class CurrentConditions:
    def __init__(self, w_report):
        self.area = w_report["current_observation"]["display_location"]["full"]
        self.condition = w_report["current_observation"]['weather']
        self.temp = w_report["current_observation"]["temperature_string"]
        self.winds = w_report["current_observation"]["wind_string"]

    def __repr__(self):
        return "Location: {}\n\nCurrent temperature: {}\nStatus: {}\nWinds: {}".format(self.area, self.temp, self.condition, self.winds)


class Suntimes:
    def __init__(self, w_report):
        self.sunrise = w_report['sun_phase']['sunrise']
        self.sunset = w_report['sun_phase']['sunset']

    def __repr__(self):
        return "Sunrise: {}:{}\nSunset: {}:{}".format(self.sunrise['hour'], self.sunrise['minute'], self.sunset['hour'], self.sunset['minute'])


class Alerts:
    def __init__(self, w_report):
        self.alerts = w_report['alerts']

    def __repr__(self):
        if self.alerts:
            return "Current weather alerts: {}".format(self.alerts)
        else:
            return "Current weather alerts: No alerts to show."


class Hurricanes:
    def __init__(self, w_report):
        self.hurricane_list = w_report['currenthurricane']

    def __repr__(self):
        if self.hurricane_list:
            names = []
            for hurricane in self.hurricane_list:
                names.append(hurricane['stormInfo']["stormName_Nice"])
            return "Storm Name: {}".format(names)
        else:
            return "Yey! No hurricanes to report."


class TenDayForecast:
    def __init__(self, w_report):
        self.forecast10day = w_report['forecast']['txt_forecast']['forecastday']

    def ten_day_forecast(self):
        day_list = []
        for day in self.forecast10day:
            day_list.append((day['title'], day['fcttext_metric']))
        return day_list

    def __repr__(self):
        day_list = self.ten_day_forecast()
        day_string = ''
        for day_info in day_list:
            day_string += "{}:\n{}\n\n".format(day_info[0], day_info[1])
        return day_string
