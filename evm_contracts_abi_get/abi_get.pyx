#!/usr/bin/env python
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import asyncio
import logging
from aiohttp_retry import ExponentialRetry
from argparse import ArgumentParser
from asyncio_throttle import Throttler
from aioetherscan import Client
from pathlib import Path
# from os.path import expanduser as _user_home_get
from os.path import join as _path_join
from os.path import exists as _path_exists
from sys import exit as sys_exit

def _log_set():
  logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO)

def _file_read(
  _file):
  try:
    with open(
      _file,
      'r') as _file_handler:
        _content = _file_handler.read()
  except FileNotFoundError as exception:
    sys_exit(
      f"ERROR: file '{_file}' not found")
  except Exception as exception:
    sys_exit(
      exception)
  return _content

def _file_write(
  _file,
  _content):
  try:
    with open(
      _file,
      'w') as _file_handler:
        _file_handler.write(
          _content)
  except FileNotFoundError as Exception:
    sys_exit(
      f"ERROR: file '{_file}' not found")
  return True

def _network_check(
  _network,
  _key):
  _network_key_needed = [
    'ethw'
  ]
  if ( _key == "" ):
    if ( _network in _network_key_needed):
      sys_exit(
        f"ERROR: network {_network} requires an API key.")


async def _client_get(
  _key_path,
  _network,
  _blockchain,
  _verbose):
  _client_kwargs={}
  _key = _key_get(
    _key_path)
  _network_check(
    _network,
    _key)
  _throttler_kwargs= {
    "rate_limit": 4,
    "period": 1.0
  }
  _throttler = Throttler(
    **_throttler_kwargs)
  _retry_options = ExponentialRetry(
    attempts=2)
  _client_kwargs = {
    "throttler": _throttler,
    "api_kind": _network,
    "network": _blockchain,
    "retry_options": _retry_options
  }
  _client = Client(
    _key,
    **_client_kwargs)
  return _client

async def _abi_get(
  _contract_address,
  _network,
  _blockchain,
  _key,
  _verbose):
  if _verbose:
    print(
      f"INFO: Connecting to {_network} ({_blockchain})")
    print(
      f"INFO: API key: {_key}")
  _client = await _client_get(
      _key,
      _network,
      _blockchain,
      _verbose)
  # if _verbose:
  #   print(
  #     _client)
  _abi = await _client.contract.contract_abi(
      _contract_address)
  await _client.close()
  return _abi
  # return _client

def _key_path_get():
  return _path_join(
    Path.home(), # _user_home_get("-"),
    ".config/etherscan/default.txt")

def _key_get(
  _path):
  if _path_exists(
       _path):
    return _file_read(
      _path)
  else:
    _msg=(
      f"WARNING: key file {_path} not found, "
      "giving the client a kirsh."
    )
    print(
      _msg)
    return "kirshkey"

def _main():
  _parser = ArgumentParser()
  _arguments = [
    [("contract_address", ),
     {"type": str,
      "help": 'address of the contract to get the ABI of.'}],
    [("--key", ),
     {'action': "store",
      "type": str,
      "default": _key_path_get(),
      "help": ('absolute path of api key '
               'of an etherscan/blockscout-like service.')}],
    [("--network", ),
     {'action': "store",
      "type": str,
      "default": 'main',
      "help": ('network to connect to '
               '(eth, bsc, avax, polygon, '
               'optimism, base, arbitrum, '
               'fantom, taiko, snowscan, '
               'gnosis, kcc, ethw, etc, '
               'doge, polygonzk, one)')}],
    [("--blockchain", ),
     {'action': "store",
      "type": str,
      "default": 'main',
      "help": ('blockchain to connect to '
               "(main, ropstein, kovan, rinkeby, "
               "goerli, sepolia, testnet, nova, hekla)")}],
    [("--output-file", ),
     {'action': "store",
      "type": str,
      "default": '',
      "help": ('path of the file in which to write '
               "the retrieved contract ABI")}],
    [("--verbose", ),
     {'dest': "verbose",
      'action': "store_true",
      "default": False,
      "help": 'extended output'}]
  ]
  for _argument in _arguments:
      _args, _kwargs = _argument
      _parser.add_argument(
        *_args,
        **_kwargs)
  _args = _parser.parse_args()
  _abi_get_args = (
    _args.contract_address,
    _args.network,
    _args.blockchain,
    _args.key,
    _args.verbose
  )
  _abi = asyncio.run(
    _abi_get(
      *_abi_get_args))
  if ( _args.output_file != "" ):
    _file_write(
      _args.output_file,
      _abi
    )
  else:
    print(
      _abi)
