import argparse
import json
import os
import random
import time

PRICE_FILE = "price_data.json"
DEFAULT_START_PRICE = 1000.0
DEFAULT_INTERVAL = 1.0
DEFAULT_VOLATILITY = 0.002  # 0.2% per tick


def write_price(price, file_path=PRICE_FILE):
    """Write the latest price to the JSON feed file."""
    payload = {"price": round(price, 2)}
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f)
        f.flush()


def simulate_price(start_price, volatility, interval, drift=0.0):
    """Generate a simple random walk price feed."""
    price = float(start_price)
    write_price(price)
    print(f"Starting price feed: {price:.2f} -> writing {PRICE_FILE}")

    try:
        while True:
            step = random.normalvariate(drift, volatility) * price
            price = max(0.01, price + step)
            write_price(price)
            print(f"Updated price: {price:.2f}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nExchange stopped by user.")


def create_initial_file(start_price):
    """Create price_data.json if it does not already exist."""
    if not os.path.exists(PRICE_FILE):
        write_price(start_price)
        print(f"Created initial {PRICE_FILE} with price {start_price:.2f}")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple Exchange price feed generator for Algo 17.")
    parser.add_argument("--start", type=float, default=DEFAULT_START_PRICE, help="Starting price")
    parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL, help="Seconds between ticks")
    parser.add_argument("--volatility", type=float, default=DEFAULT_VOLATILITY, help="Tick volatility as a fraction of price")
    parser.add_argument("--drift", type=float, default=0.0, help="Optional drift per tick as a fraction of price")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    create_initial_file(args.start)
    simulate_price(args.start, args.volatility, args.interval, args.drift)
