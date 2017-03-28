import requests
import os
import time
from w_classes import CurrentConditions
from w_classes import Suntimes
from w_classes import Alerts
from w_classes import Hurricanes
from w_classes import TenDayForecast


def clear():
    os.system('clear')


def main():
    clear()
    print("\t\tWelcome to Weather Underground\n")
    zipcode = int(input("Enter a zipcode (XXXXX) for weather information: "))
    r = requests.get("http://api.wunderground.com/api/"
                     "844b5d5e3bb67013/conditions/forecast10day/astronomy/"
                     "alerts/currenthurricane/q/{}.json".format(zipcode))
    w_report = r.json()
    interface(w_report)


def interface(w_report):
    c = CurrentConditions(w_report)
    s = Suntimes(w_report)
    a = Alerts(w_report)
    h = Hurricanes(w_report)
    t = TenDayForecast(w_report)
    print("\n")
    print(c)
    time.sleep(0.8)
    print("\n")
    print(s)
    time.sleep(1)
    print("\n")
    print(a)
    time.sleep(1)
    print("\n")
    print(h)
    print("\n")
    print("--- 10 day forecast ---\n\n")
    time.sleep(1.5)
    print(t)
    print("\n")
    input("Scroll up or press ENTER to return to command line.")


if __name__ == "__main__":
    main()
