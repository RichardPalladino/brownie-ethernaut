# Template to deploy solidity contract to a blockchain
from brownie import network, config, accounts, Fallback, Fallout, CoinFlip

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account() -> str:
    if (
        network.show_active() in LOCAL_BLOCKCHAINS
        or network.show_active() in BLOCKCHAIN_FORKS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_fallback_contract() -> Fallback:
    account = get_account()
    print(f"Deploying fallback vulnerable contract from {account}....")
    contract = Fallback.deploy({"from": account})
    print("Success! Fallback contract deployed at {}".format(contract.address))
    return contract


def deploy_fallout_contract() -> Fallout:
    account = get_account()
    print(f"Deploying fallback vulnerable contract from {account}....")
    contract = Fallout.deploy({"from": account})
    print("Success! Fallback contract deployed at {}".format(contract.address))
    return contract


def deploy_coinflip_contract() -> CoinFlip:
    account = get_account()
    print(f"Deploying fallback vulnerable contract from {account}....")
    contract = CoinFlip.deploy({"from": account})
    print("Success! CoinFlip contract deployed at {}".format(contract.address))
    return contract
