import requests
from w_classes import CurrentConditions, Suntimes, Alerts, Hurricanes, TenDayForecast


def main():
    zipcode = int(input("What zipcode: "))
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
    print("\n")
    print(s)
    print("\n")
    print(a)
    print("\n")
    print(h)
    print("\n")
    print(t)
    print("\n")


if __name__ == "__main__":
    main()
