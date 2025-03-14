"""Setup for EVM contracts ABI get"""
from setuptools import setup, find_packages
from Cython.Build import cythonize

with open(
  "README.md",
  "r") as fh:
  long_description = fh.read()

_name = "evm-contracts-abi-get"
_version = "0.0.0.0.0.0.0.0.0.0.0.1.1.1.1.1.1"
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
  'entry_points': {
    'console_scripts': [
      'evm-contracts-abi-get = evm_contracts_abi_get:_main']
  },
  'install_requires': [
    'aioetherscan >= 0.9.6',
    'cython',
  ],
  'classifiers': [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    "Operating System :: Unix",
  ],
  'ext_modules':
    cythonize(
      'evm_contracts_abi_get/abi_get.pyx'),
}
setup(
  **_setup_kwargs)
