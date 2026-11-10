"""Tests for safe location handling in weather.py."""

from unittest import mock

import weather


def _get_url(location, style="brief"):
    with mock.patch.object(weather.requests, "get") as get:
        get.return_value.text = "ok"
        get.return_value.raise_for_status = lambda: None
        weather.fetch_weather(location, style)
        return get.call_args[0][0]


def test_location_with_spaces_is_encoded():
    assert _get_url("New York") == "https://wttr.in/New%20York"


def test_location_cannot_escape_path_or_query():
    url = _get_url("London/Paris?lang=fr#frag")
    assert url == "https://wttr.in/London%2FParis%3Flang%3Dfr%23frag"


def test_plus_convention_from_cli_is_preserved():
    # main() encodes spaces as "+"; that convention keeps working.
    assert _get_url("New+York") == "https://wttr.in/New+York"


def test_non_ascii_location_is_encoded():
    url = _get_url("São Paulo")
    assert " " not in url
    assert url.startswith("https://wttr.in/")
