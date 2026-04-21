from bt_api_base.containers.exchanges.exchange_data import ExchangeData

__all__ = ["ExmoExchangeData", "ExmoExchangeDataSpot"]


class ExmoExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "exmo"
        self.rest_url = "https://api.exmo.com/v1.1"
        self.wss_url = "wss://ws.exmo.me/v1.1"
        self.kline_periods = {
            "1m": "1",
            "5m": "5",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "2h": "120",
            "4h": "240",
            "1d": "D",
            "1w": "W",
            "1M": "M",
        }
        self.legal_currency = [
            "USDT",
            "USD",
            "EUR",
            "UAH",
            "RUB",
            "GBP",
            "PLN",
            "TRY",
            "BTC",
            "ETH",
        ]


class ExmoExchangeDataSpot(ExmoExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "spot"
        self.rest_paths = {}
        self.wss_paths = {}
