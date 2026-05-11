# Algo 19: HMA Trend Algo

## Overview
This is a trend-following algorithm using Hull Moving Averages (HMA) for low-lag trend detection. It uses a fast HMA (9-period) and slow HMA (21-period) to generate buy/sell signals on crossovers. Includes take-profit (+0.5%) and stop-loss (-1%) exits.

The algorithm can be tested backward (historical data) or forward (live simulation).

## Prerequisites
- Python 3.x installed
- All scripts in the `Algo 19 HMA Trend Algo` directory
- For backtesting: Historical data in `data/` folder (use `data_download.py` if needed)

## Backward Testing (Historical Data)

### 1. Download Data (`data_download.py`)
This script downloads historical price data for backtesting.

**Command:**
```bash
python data_download.py
```

**Flow:**
- Downloads data (e.g., from Yahoo Finance or similar).
- Saves to `data/` folder (e.g., CSV files).
- Run this first if `data/` is empty.

### 2. Run Backtest (`backtest_algo_19.py`)
Tests the algorithm on historical data, generating performance reports.

**Command:**
```bash
python backtest_algo_19.py
```

**Parameters:** Hardcoded in script (adjust as needed):
- HMA periods: Fast=9, Slow=21
- TP: +0.5%, SL: -1%
- Capital: 100,000
- Units: 100 per trade

**Flow:**
1. Loads historical data from `data/` (e.g., CSV with OHLC).
2. Calculates HMA for each candle.
3. Simulates trades on HMA crossovers.
4. Generates reports in `reports/` (e.g., PnL, drawdown, Sharpe ratio).
5. Outputs summary to console and files.

**Outputs:**
- Console: Trade log, final PnL, metrics.
- Files: `reports/backtest_results.csv`, charts, etc.

## Forward Testing (Live Simulation)

### 1. Start Price Feed (`Exchange.py`)
Simulates live price updates for forward testing.

**Command:**
```bash
python Exchange.py --start 1000 --interval 1.0 --volatility 0.002 --drift 0.0
```

**Parameters:**
- `--start` (float, default: 1000.0): Initial price.
- `--interval` (float, default: 1.0): Seconds between updates.
- `--volatility` (float, default: 0.002): Price volatility (0.2% per tick).
- `--drift` (float, default: 0.0): Optional upward/downward bias.

**Flow:**
1. Creates/updates `price_data.json` with simulated prices.
2. Runs indefinitely, updating prices every interval.
3. Stop with Ctrl+C.

### 2. Run Live Algo (`Algo 19.py`)
Executes trades based on live price feed.

**Command:**
```bash
python "Algo 19.py"
```

**Parameters:** Hardcoded (same as backtest).

**Flow:**
1. Waits for 21 prices to seed HMAs.
2. Monitors HMA crossovers for entries.
3. Manages positions with TP/SL.
4. Prints real-time PnL, unrealized PnL.
5. Runs until stopped (Ctrl+C), shows final PnL.

## Running Both Tests
- **Backward First:** Use `backtest_algo_19.py` to validate strategy on history.
- **Forward After:** Use `Exchange.py` + `Algo 19.py` for real-time simulation.
- Run scripts in separate terminals for forward testing.

## Notes
- Adjust HMA lengths, TP/SL in scripts for tuning.
- Backtest uses static data; forward uses random walk.
- Reports in `reports/` for backtest analysis.
- Stop any running script with Ctrl+C.