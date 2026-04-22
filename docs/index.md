# EXMO Documentation

## English

Welcome to the EXMO documentation for bt_api.

### Quick Start

```bash
pip install bt_api_exmo
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "EXMO___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("EXMO___SPOT", "BTCUSDT")
print(ticker)
```

## 中文

欢迎使用 bt_api 的 EXMO 文档。

### 快速开始

```bash
pip install bt_api_exmo
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "EXMO___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("EXMO___SPOT", "BTCUSDT")
print(ticker)
```

## API Reference

See source code in `src/bt_api_exmo/` for detailed API documentation.
