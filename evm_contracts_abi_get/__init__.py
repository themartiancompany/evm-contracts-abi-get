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
  except FileNotFoundException as Exception:
    print(
      f"ERROR: file '{_file}' not found")
  return _content

async def _client_get(
  _etherscan_key_path,
  _verbose):
  _etherscan_key = _file_read(
    _etherscan_key_path)
  _throttler = Throttler(
    rate_limit=4,
    period=1.0)
  _retry_options = ExponentialRetry(
    attempts=2)
  _client = Client(
    _etherscan_key,
    throttler=_throttler,
    retry_options=_retry_options)
  return _client

async def _abi_get(
  _contract_address,
  _etherscan_key,
  _verbose):
  if _verbose:
    print(
      f"INFO: Etherscan key: {_etherscan_key}")
  _client = await _client_get(
      _etherscan_key,
      _verbose)
  # if _verbose:
  #   print(
  #     _client)
  _abi = await _client.contract.contract_abi(
      _contract_address)
  await _client.close()
  return _abi
  # return _client

def _etherscan_key_get():
  return _path_join(
    Path.home(), # _user_home_get("-"),
    ".config/etherscan/default.txt")

def _main():
  _parser = ArgumentParser()
  _arguments = [
    [("contract_address", ),
     {"type": str,
      "help": 'absolute path of input file'}],
    [("--etherscan_key", ),
     {'action': "store",
      "type": str,
      "default": _etherscan_key_get(),
      "help": 'absolute path of etherscan key'}],
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
    _args.etherscan_key,
    _args.verbose
  )
  _abi = asyncio.run(
    _abi_get(
      *_abi_get_args))
  print(
    _abi)

if __name__ == "__main__":
  _main()
