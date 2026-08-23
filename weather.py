#!/usr/bin/env python3
"""Fetch current weather for any city using the free wttr.in service."""

import argparse
import sys

import requests

FORMATS = {
    "brief": "3",
    "full": "",
    "oneline": "%l: %c %t (feels like %f), wind %w, humidity %h",
}


def fetch_weather(location: str, style: str) -> str:
    url = f"https://wttr.in/{location}"
    params = {"format": FORMATS[style], "lang": "en"}
    headers = {"User-Agent": "curl/8.0"}  # wttr.in serves plain text to curl agents

    response = requests.get(url, params=params, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text.strip()


def main():
    parser = argparse.ArgumentParser(description="Weather from wttr.in")
    parser.add_argument("location", nargs="?", default="",
                        help="City name, e.g. 'Delhi' or 'Kolkata'")
    parser.add_argument("-s", "--style", choices=FORMATS.keys(), default="brief",
                        help="Output detail level")
    args = parser.parse_args()

    location = args.location.replace(" ", "+") if args.location else ""
    try:
        print(fetch_weather(location, args.style))
    except requests.exceptions.HTTPError:
        sys.exit(f"Could not find weather for '{args.location}'. Check the spelling.")
    except requests.exceptions.RequestException as e:
        sys.exit(f"Network error: {e}")


if __name__ == "__main__":
    main()
