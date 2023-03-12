from brownie import network, config, accounts, web3, CoinFlip
import brownie.convert

# from web3 import Web3
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]
TESTNETS = ["goerli", "sepolia"]


def get_account() -> str:
    if (
        network.show_active() in LOCAL_BLOCKCHAINS
        or network.show_active() in BLOCKCHAIN_FORKS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main() -> None:
    if (network.show_active() in BLOCKCHAIN_FORKS) or (
        network.show_active() in TESTNETS
    ):
        account = get_account()
        # print(f"Web3 connected?  {w3.isConnected()}")
        last_block = web3.eth.get_block("latest")
        print(
            f"Block number {last_block['number']} has hash {brownie.convert.to_uint(last_block['hash'])}"
        )
        coinflip = CoinFlip.deploy({"from": account})
        last_block = web3.eth.get_block("latest")
        print(
            f"Block number {last_block['number']} has hash {brownie.convert.to_uint(last_block['hash'])}"
        )


if __name__ == "__main__":
    main()
