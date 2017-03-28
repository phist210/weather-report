import json
from w_classes import CurrentConditions
from w_classes import Suntimes
from w_classes import Alerts
from w_classes import Hurricanes
from w_classes import TenDayForecast


with open('report.json') as f:
    report = json.load(f)


def test_CCinit():
    conditions = CurrentConditions(report)
    return conditions


def test_Sinit():
    suntimes = Suntimes(report)
    return suntimes


def test_Ainit():
    alerts = Alerts(report)
    return alerts


def test_Hinit():
    hurricanes = Hurricanes(report)
    return hurricanes


def test_10init():
    ten_day_forecast = TenDayForecast(report)
    return ten_day_forecast
