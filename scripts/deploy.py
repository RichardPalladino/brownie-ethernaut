# Template to deploy solidity contract to a blockchain
from brownie import (
    network,
    config,
    accounts,
    Fallback,
    Fallout,
    CoinFlip,
    Telephone,
    AttackTelephone,
    Token,
    Delegate,
    Delegation,
    AttackDelegation,
    AttackCoinflip,
)

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]
TESTNETS = ["goerli", "sepolia"]


def get_account() -> str:
    if (
        network.show_active() in LOCAL_BLOCKCHAINS
        or network.show_active() in BLOCKCHAIN_FORKS
    ):
        return accounts[0]
    elif network.show_active() in TESTNETS:
        return accounts.add(config["networks"][network.show_active()]["wallet"])
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


def deploy_telephone_contract() -> Telephone:
    account = get_account()
    print(f"Deploying telephone contract from {account}....")
    contract = Telephone.deploy({"from": account})
    print("Success! Telephone contract deployed at {}".format(contract.address))
    return contract


def deploy_telephone_attack(_telephone_contract) -> AttackTelephone:
    account = accounts[2]
    print(f"Deploying telephone attack contract from {account}....")
    contract = AttackTelephone.deploy(_telephone_contract, {"from": account})
    print("Success! Telephone attack contract deployed at {}".format(contract.address))
    return contract


def deploy_token_underflow(_starting_ammount) -> Token:
    account = get_account()
    print(f"Deploying token contract vulnerable to underflow from {account}....")
    contract = Token.deploy(_starting_ammount, {"from": account})
    print("Success! Token contract deployed at {}".format(contract.address))
    return contract


def deploy_delegate_contracts() -> Delegation:
    account = get_account()
    print(f"Deploying delegate contract from {account}....")
    contract = Delegate.deploy(account.address, {"from": account})
    print(f"Deploying delegation contract from {account}....")
    contract = Delegation.deploy(contract.address, {"from": account})
    print("Success! Delegation contract deployed at {}".format(contract.address))
    return contract


def deploy_attack_delegation(_delegation_contract) -> AttackDelegation:
    account = accounts[2]
    print(
        f"Deploying attack contract from {account} to attack {_delegation_contract}...."
    )
    contract = AttackDelegation.deploy(_delegation_contract, {"from": account})
    print("Success! Delegation attack contract deployed at {}".format(contract.address))
    return contract


def deploy_attack_coinflip(_coinflip_contract) -> AttackCoinflip:
    account = get_account()
    print(
        f"Deploying attack contract from {account} to attack {_coinflip_contract}...."
    )
    contract = AttackCoinflip.deploy(_coinflip_contract, {"from": account})
    print("Success! Coinflip attack contract deployed at {}".format(contract.address))
    return contract
