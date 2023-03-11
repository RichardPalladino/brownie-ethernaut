# Template to deploy solidity contract to a blockchain
from brownie import network, config, accounts, Fallback

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
LOCAL_BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]


def deploy_fallback_contract() -> Fallback:
    account = accounts[0]
    print(f"Deploying fallback vulnerable contract from {account}....")
    contract = Fallback.deploy({"from": account})
    print("Success! Fallback contract deployed at {}".format(contract.address))
    return contract
