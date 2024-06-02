import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
from app.services.financeService.PolygonApiService import PolygonApiService

@pytest.fixture
def polygon_service():
    return PolygonApiService()

@patch('app.services.financeService.PolygonApiService.requests.get')
def test_get_dia_util_with_holiday(mock_requests_get, polygon_service):
    # Mocking response from the API
    mock_response = MagicMock()
    mock_response.json.return_value = [{"date": "2024-07-04"}]
    mock_requests_get.return_value = mock_response
    
    # Testing with a holiday
    date_to_check = datetime(2024, 7, 4)
    expected_result = datetime(2024, 7, 3)
    assert polygon_service._getDiaUtil(date_to_check) == expected_result


@patch('app.services.financeService.PolygonApiService.PolygonApiService._getDiaUtil')
@patch('app.services.financeService.PolygonApiService.RESTClient.get_grouped_daily_aggs')
@patch('app.services.financeService.PolygonApiService.requests.get')
def test_carregar_acoes(mock_requests_get, mock_get_grouped_daily_aggs, mock_get_dia_util, polygon_service):
    # Mocking responses
    mock_ticker_details = MagicMock()
    mock_ticker_details.json.return_value = {
        "results": [{"ticker": "AAPL", "name": "Apple Inc."}]
    }
    mock_requests_get.side_effect = [mock_ticker_details]
    
    mock_daily_aggs = [
        MagicMock(ticker="AAPL", open=100.0, high=110.0, low=90.0, close=105.0, volume=1000000,
                  vwap=100.0, transactions=1000)
    ]
    mock_get_grouped_daily_aggs.return_value = mock_daily_aggs
    
    mock_get_dia_util.return_value = datetime(2024, 7, 5)  # A Friday
    
    # Running the method to be tested
    result = polygon_service.carregarAcoes()
    
    # Assertions
    expected_result = {
        "AAPL": {
            "name": "Apple Inc.",
            "ticker": "AAPL",
            "open": 100.0,
            "high": 110.0,
            "low": 90.0,
            "close": 105.0,
            "volume": 1000000,
            "vwap": 100.0,
            "transactions": 1000
        }
    }
    assert result == expected_result
