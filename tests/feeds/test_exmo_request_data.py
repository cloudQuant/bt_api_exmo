from unittest.mock import MagicMock
from bt_api_exmo.feeds.live_exmo.request_base import ExmoRequestData
def test_exmo_disconnect_closes_http_client() -> None:
    request_data = ExmoRequestData()
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()
