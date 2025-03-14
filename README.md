[comment]: <> (SPDX-License-Identifier: AGPL-3.0)

[comment]: <> (-------------------------------------------------------------)
[comment]: <> (Copyright © 2024, 2025  Pellegrino Prevete)
[comment]: <> (All rights reserved)
[comment]: <> (-------------------------------------------------------------)

[comment]: <> (This program is free software: you can redistribute)
[comment]: <> (it and/or modify it under the terms of the GNU Affero)
[comment]: <> (General Public License as published by the Free)
[comment]: <> (Software Foundation, either version 3 of the License.)

[comment]: <> (This program is distributed in the hope that it will be useful,)
[comment]: <> (but WITHOUT ANY WARRANTY; without even the implied warranty of)
[comment]: <> (MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the)
[comment]: <> (GNU Affero General Public License for more details.)

[comment]: <> (You should have received a copy of the GNU Affero General Public)
[comment]: <> (License along with this program.)
[comment]: <> (If not, see <https://www.gnu.org/licenses/>.)

# EVM Contracts ABI Get (`evm-contracts-abi-get`)

Cythonized Python program which retrieves from online sources
and returns the ABI of a smart contract on an
Ethereum Virtual Machine (EVM) compatible network.

This program is a software dependency for the
[EVM Contracts Tools](
  https://github.com/themartiancompany/evm-contracts-tools)
and depends on
[The Martian Company](
  https://github.com/themartiancompany)'s
fork of
[Aioetherscan](
  https://themartiancompany/aioetherscan).

## Installation

The program in this source repo
can be installed from source using Python's setuptools.

```bash
# Build
python \
  setup.py \
    build
# Install
python \
  setup.py \
    install
```

The collection has officially published on the
the uncensorable
[Ur](
  https://github.com/themartiancompany/ur)
user repository and application store as
`evm-contracts-abi-get`.
The source code is published on the
[Ethereum Virtual Machine File System](
  https://github.com/themartiancompany/evmfs)
so it can't possibly be taken down.

To install it from there just type

```bash
ur \
  evm-contracts-abi-get
```

A censorable HTTP Github mirror of the recipe published there,
containing a full list of the software dependencies needed to run the
tools is hosted on
[evm-contracts-abi-get-ur](
  https://github.com/themartiancompany/evm-contracts-abi-get-ur).
Be aware the mirror could go offline any time as Github and more
in general all HTTP resources are inherently unstable and censorable.

## License

This program is released by Pellegrino Prevete (aka Truocolo)
under the terms of the GNU Affero General Public License version 3.
