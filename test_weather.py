import requests
import requests_mock


with requests_mock.Mocker() as m:
    m.get('http://api.wunderground.com/api/844b5d5e3bb67013/condition/forecast10day/astronomy/alerts/currenthurricane/q/27703.json', text='resp')
    requests.get('http://api.wunderground.com/api/844b5d5e3bb67013/condition/forecast10day/astronomy/alerts/currenthurricane/q/27703.json').text
