"""
Tests for wrapper for GarlandTools Item Endpoint
"""

from . import data


def test_data_is_ok():
    """
    Tests if an data request succeeds
    """
    response = data()
    assert response.ok


def test_data_is_json():
    """
    Tests if an data request returns JSON
    """
    response = data()
    response_json = response.json()
    assert isinstance(response_json, dict)