# 0xAfF0E31297888F3Bff5aA6F6DEe02bB7143bd767

# import web3
import brownie.convert
from brownie import network, config, accounts, interface, web3

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


def main() -> None:
    if network.show_active() == "goerli":
        # I can use this approach with Vault, since I don't see any equivalent "get_storage_at" function native to Brownie
        test_val = web3.eth.get_storage_at(
            "0xAfF0E31297888F3Bff5aA6F6DEe02bB7143bd767", 1
        )
        print(test_val)


if __name__ == "__main__":
    main()
