from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network
import pytest
from scripts.deploy_and_create import deploy_and_create


def test_can_create_simple_Collectible():
    if network.show_active not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()