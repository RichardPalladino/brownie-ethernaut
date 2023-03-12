from brownie import network, config, accounts, web3, CoinFlip
import brownie.convert

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


def test_coinflip_prediction():
    if (network.show_active() in BLOCKCHAIN_FORKS) or (
        network.show_active() in TESTNETS
    ):
        # Arrange
        account = get_account()
        # print(f"Web3 connected?  {w3.isConnected()}")
        last_block = web3.eth.get_block("latest")
        last_block_hash = brownie.convert.to_uint(last_block["hash"])
        coinflip = CoinFlip.deploy({"from": account})

        # Act
        count = 0
        while count < 10:
            last_block = web3.eth.get_block("latest")
            last_block_hash = brownie.convert.to_uint(last_block["hash"])
            result_num = (
                last_block_hash
                // 57896044618658097711785492504343953926634992332820282019728792003956564819968
            )
            result_bool = result_num == 1
            tx = coinflip.flip(result_bool, {"from": account})
            count += 1
        # Assert
        assert coinflip.consecutiveWins() >= 10
