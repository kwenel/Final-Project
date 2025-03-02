import pytest
import requests
from unittest.mock import patch
from project import get_access_token, get_flight_prices

MOCK_ACCESS_TOKEN = "mock_access_token"

MOCK_FLIGHT_PRICES = [
    ["AirlineA", "$300"],
    ["AirlineB", "$250"],
    ["AirlineC", "$400"]
]

@pytest.fixture
def mock_access_token():
    """Fixture to mock get_access_token() response."""
    with patch("project.requests.post") as mock_post:
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"access_token": MOCK_ACCESS_TOKEN}
        yield mock_post

@pytest.fixture
def mock_flight_prices():
    """Fixture to mock get_flight_prices() API response."""
    with patch("project.requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {"price": {"total": "300"}, "itineraries": [{"segments": [{"carrierCode": "AirlineA"}]}]},
                {"price": {"total": "250"}, "itineraries": [{"segments": [{"carrierCode": "AirlineB"}]}]},
                {"price": {"total": "400"}, "itineraries": [{"segments": [{"carrierCode": "AirlineC"}]}]}
            ]
        }
        yield mock_get

def test_get_access_token(mock_access_token):
    """Test that get_access_token retrieves the correct token."""
    token = get_access_token()
    assert token == MOCK_ACCESS_TOKEN

def test_get_flight_prices(mock_access_token, mock_flight_prices):
    """Test that get_flight_prices returns expected flight data."""
    flights = get_flight_prices("NYC", "LAX", "2025-03-10")
    
    assert isinstance(flights, list)
    assert len(flights) == 3
    assert flights[0] == ["AirlineA", "$300"]
    assert flights[1] == ["AirlineB", "$250"]
    assert flights[2] == ["AirlineC", "$400"]

def test_get_flight_prices_failed_auth():
    """Test get_flight_prices when authentication fails (invalid access token)."""
    with patch("project.get_access_token", return_value=None):
        flights = get_flight_prices("NYC", "LAX", "2025-03-10")
        assert flights is None

def test_get_flight_prices_api_failure():
    """Test get_flight_prices when API returns an error."""
    with patch("project.get_access_token", return_value=MOCK_ACCESS_TOKEN):
        with patch("project.requests.get") as mock_get:
            mock_get.return_value.status_code = 500  
            flights = get_flight_prices("NYC", "LAX", "2025-03-10")
            assert flights is None