"""Setup for EVM contract ABI get"""
from setuptools import setup, find_packages

with open(
  "README.md",
  "r") as fh:
  long_description = fh.read()

_name = "evm-contract-abi-get"
_version = "0.0.0.0.0.0.0.0.0.0.0.0.1"
_setup_kwargs={
  'name': f"{_name}",
  'version': f"{_version}",
  'author': "Pellegrino Prevete",
  'author_email': "pellegrinoprevete@gmail.com",
  'description': "Get ABI of a smart contract on an EVM network.",
  'long_description': long_description,
  'long_description_content_type': "text/markdown",
  'url': f"https://github.com/themartiancompany/{_name}",
  'packages': find_packages(),
  'package_data': {},
  'entry_points': {
    'console_scripts': [
      'evm-contract-abi-get = evm_contract_abi_get:_main']
  },
  'install_requires': [
    'appdirs',
    'aioetherscan',
  ],
  'classifiers': [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    "Operating System :: Unix",
  ]
}
setup(
  **_setup_kwargs)
