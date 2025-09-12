# ...existing code...
import requests
import json
import os
from datetime import datetime

def fetch_and_save_prices():
    inp = input("Enter symbol(s) (comma-separated, e.g. BTCUSDT,ETHUSDT) or press Enter for BTCUSDT: ").strip()
    symbols = [s.strip().upper() for s in inp.split(",") if s.strip()] or ["BTCUSDT"]
    url = "https://api.binance.com/api/v3/ticker/price"
    new_results = []

    for sym in symbols:
        try:
            resp = requests.get(url, params={"symbol": sym}, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            price = data.get("price")
            print(f"{sym}: {price}")
            new_results.append({
                "symbol": data.get("symbol"),
                "price": price,
                "fetched_at": datetime.utcnow().isoformat() + "Z"
            })
        except requests.RequestException as e:
            print(f"Error fetching {sym}: {e}")

    out_path = r"d:\LEarninig\Learning\prices.json"

    # load existing entries (if any) and append new ones
    existing = []
    if os.path.exists(out_path):
        try:
            with open(out_path, "r", encoding="utf-8") as f:
                existing = json.load(f) or []
        except Exception:
            existing = []

    existing.extend(new_results)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=4)

    print("Saved:", os.path.abspath(out_path))

if __name__ == "__main__":
    fetch_and_save_prices()
# ...existing code...