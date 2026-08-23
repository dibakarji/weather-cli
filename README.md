# Weather CLI ⛅

Current weather for any city, fetched from [wttr.in](https://wttr.in) - no API key required.

## Features

- Three output styles: one-line, brief 3-day, or full ASCII forecast
- Handles multi-word cities ("New York", "Kolkata")
- Friendly errors for unknown locations

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python weather.py Delhi
python weather.py "New York" --style full
python weather.py Mumbai --style oneline
```

## Example

```
$ python weather.py Delhi --style oneline
Delhi: ☀️ +34°C (feels like +38°C), wind → 12km/h, humidity 41%
```

---
Part of my **31 Python Projects** challenge - one small, genuine project at a time.
