from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _exmo_balance_handler
from bt_api_exmo.exchange_data import ExmoExchangeDataSpot
from bt_api_exmo.feeds.live_exmo.spot import ExmoRequestDataSpot
from bt_api_base.registry import ExchangeRegistry


def register_exmo() -> None:
    ExchangeRegistry.register_feed("EXMO___SPOT", ExmoRequestDataSpot)
    ExchangeRegistry.register_exchange_data("EXMO___SPOT", ExmoExchangeDataSpot)
    ExchangeRegistry.register_balance_handler("EXMO___SPOT", _exmo_balance_handler)


register_exmo()
