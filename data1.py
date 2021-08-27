import requests

api_key = "5138716b65d6565a66c35a343bf0b255"
end_point = "https://api.openweathermap.org/data/2.5/weather"
parameter = {
    "zip": "55106,us",
    "appid": api_key,
    "units": "metric"
}

end_point2 = "http://api.positionstack.com/v1/forward"
api_key2 = "022543f6441889e72c6479b1a7df991a"
parameter2 = {
    "access_key": api_key2,
    "query": 55106
}


class Data:
    def __init__(self):
        self.api_key = api_key
        self.end_point = end_point
        self.parameter = parameter
        self.parameter2 = parameter2

    def fetch_weather(self, zc):
        global parameter
        zc = str(zc)
        zc += ",us"
        self.parameter["zip"] = zc
        self.response = requests.get(url=end_point, params=self.parameter)
        self.response.raise_for_status()
        self.weather_data = self.response.json()
        return self.weather_data

    def fetch_temp(self, zc):
        zc = str(zc)
        self.data = self.fetch_weather(zc)
        self.temp = self.data["main"]["temp"]
        self.temp = round(self.temp)
        return self.temp
    def fetch_name(self, zc):
        zc = str(zc)
        self.data = self.fetch_weather(zc)
        self.city_name = self.data["name"]
        return self.city_name
    def fetch_condition(self, zc):
        zc = str(zc)
        self.data = self.fetch_weather(zc)
        self.condition = self.data["weather"][0]["description"]
        return self.condition
    def fetch_state(self, zc):
        global parameter2
        self.parameter2["query"] = zc
        self.response2 = requests.get(url=end_point2, params=parameter2)
        self.zip_data = self.response2.json()
        self.state = self.zip_data["data"][0]["region_code"]
        return self.state












