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
        last_block_hash = brownie.convert.to_uint(last_block["hash"])
        print(f"Block number {last_block['number']} has hash {last_block_hash}")
        coinflip = CoinFlip.deploy({"from": account})

        count = 0
        while count < 10:
            last_block = web3.eth.get_block("latest")
            last_block_hash = brownie.convert.to_uint(last_block["hash"])
            print(f"Block number {last_block['number']} has hash {last_block_hash}")
            result_num = (
                last_block_hash
                // 57896044618658097711785492504343953926634992332820282019728792003956564819968
            )

            if result_num == 0:
                result_bool = False
                print(
                    f"Division result is {result_num}. Predict next result will be {result_bool}"
                )
            elif result_num == 1:
                result_bool = True
                print(
                    f"Division result is {result_num}. Predict next result will be {result_bool}"
                )
            else:
                print(f"The result {result_num} breaks my assumptions.")
            tx = coinflip.flip(result_bool, {"from": account})
            print(f"Consecutive wins: {coinflip.consecutiveWins()}")
            count += 1


if __name__ == "__main__":
    main()
