from brownie import reverts, accounts

from scripts.deploy import deploy_telephone_contract, deploy_telephone_attack


def test_telephone_attack():
    ## Arrange
    telephone_contract = deploy_telephone_contract()
    attacker = accounts[2]
    # Assert
    assert telephone_contract.owner() != attacker.address
    ## Attack at deployment
    telephone_attack = deploy_telephone_attack(telephone_contract.address)
    ## Assert
    assert telephone_contract.owner() == attacker.address
