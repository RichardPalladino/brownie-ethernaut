// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// There are methods to read a contract's memory slots, even if private
// This was easy enough.
// Can be done with pretty much any web3 framework or library
// read slot1 (bool takes one slot, bytes32 takes the other, start at 0)
contract Vault {
  bool public locked;
  bytes32 private password;

  constructor(bytes32 _password) {
    locked = true;
    password = _password;
  }

  function unlock(bytes32 _password) public {
    if (password == _password) {
      locked = false;
    }
  }
}