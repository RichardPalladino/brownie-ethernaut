"""
This script is a WIP.  I'm using the Ethernaut challenges to try and understand eth-brownie and web3.py better.
These are not as well documented or straightforward of frameworks as Hardhat or Foundry even, but Python has its advantages at times.
"""

from brownie import (
    network,
    config,
    accounts,
    Fallout,
)


LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account() -> str:
    if (
        network.show_active() in LOCAL_BLOCKCHAINS
        or network.show_active() in BLOCKCHAIN_FORKS
    ):
        return accounts[0]
    else:
        return accounts.add(config["networks"][network.show_active()]["wallet"])


def main() -> None:
    account = get_account()
    print(account.address)
    # contract = Fallout("0x530A83576199eE805Db3EA6CfC437892B9c69Dd9")
    # print(contract.address)


# this is incomplete.... leaving it incomplete because I just used Remix to beat the level itself.
# need to ues interfaces

if __name__ == "__main__":
    main()
