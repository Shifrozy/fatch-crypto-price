...existing code...
# Binance Price Fetcher

Lightweight Python utility to fetch current prices from Binance and append results to a local JSON file.

## Files
- `save_prices.py` — main script (prompt for symbols, fetch, save).
- `prices.json` — stored results (array of objects).
- `README.md` — this file.

## Prerequisites
- Python 3.8+
- Install requests:
```powershell
pip install requests
```

## Usage
1. Open PowerShell or CMD.
2. Run:
```powershell
python d:\abc\abc\save_prices.py
```
3. When prompted enter one or more symbols (comma-separated), for example:
```
BTCUSDT,ETHUSDT,XRPUSDT
```
Or press Enter to default to BTCUSDT.

Results will be printed and appended to `where you are working`.

## Notes
- The script appends new entries to the JSON array. If the JSON becomes invalid, delete or reset `prices.json`.
- Binance rate limits apply; avoid rapid repeated requests.
- To store additional fields (24h change, volume) use `/api/v3/ticker/24hr`.

## License
MIT