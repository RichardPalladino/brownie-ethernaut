// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

interface ICoinFlip {
    function consecutiveWins() external returns (uint256);
    function flip(bool _guess) external returns (bool);
}