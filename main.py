"""
# Star Watch

Check what are the best days to watch stars taking into account the moon cycle and the weather. 

Command line options:
- from: starting day (defaults to today)
- during: number of days to consider (defaults to 7 days)
"""

import click
from pprint import pprint
import requests
import pylunar
import datetime

@click.command()
@click.option('--from', 'from_', default='today', type=click.Choice(['today', 'tomorrow', 'day after tomorrow']), help='day from which you want to have the forecast')
@click.option('--during', default=7, help='number of days of the forecast: from 1 to 10')
def main(from_, during):
    url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/17105"
    querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJlcG9uc2NAZ21haWwuY29tIiwianRpIjoiZjJmYzNhYTEtYmM4OC00ZTkyLTgyMTctOTI0MzdiZTI5NTkxIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1NjkyNjEyNTAsInVzZXJJZCI6ImYyZmMzYWExLWJjODgtNGU5Mi04MjE3LTkyNDM3YmUyOTU5MSIsInJvbGUiOiIifQ.pD9llUZtFQqJCwpDjj8BG_deFOm7R5tSoJNxkBFWOfU"}
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.get(url, headers=headers, params=querystring)
    url_municipi = response.json()["datos"]
    response = requests.get(url_municipi, headers=headers, params=querystring)
    prediction = response.json()[0]["prediccion"]["dia"]
    
    daily_sky_status = []
    for day in prediction:
        daily_sky_status.append(day["estadoCielo"][-1]["descripcion"])
    
    one_day = datetime.timedelta(days=1)
    today = datetime.date.today()
    days = []
    for x in range(7):
        days.append(today + one_day * x)

    mi = pylunar.MoonInfo((42, 7, 30), (2, 38, 19))

    daily_moon_phase = []
    days_string = []

    for x in days:
        mi.update((x.year, x.month, x.day, 22, 0, 0))
        daily_moon_phase.append(mi.fractional_phase())
        days_string.append(x.strftime("%d/%m/%Y"))

    preresult = list(zip(daily_sky_status, daily_moon_phase))

    result = []
    for sky_status, moon_phase in preresult:
        if moon_phase < 0.5 and sky_status in ["Despejado", "Despejado noche", "Poco nuboso", "Poco nuboso noche"]:
            result.append("Very Good Night for stargazing")
        elif moon_phase < 0.5 and sky_status in ["Intervalos nubosos", "Intervalos nubosos noche"]:
            result.append("Good Night for stargazing")
        elif moon_phase < 0.2 and sky_status in ["Despejado", "Despejado noche", "Poco nuboso", "Poco nuboso noche"]:
            result.append("Perfect Night for stargazing")
        else:
            result.append("Another Night would be better")
    final_result = list(zip(days_string, result))
    pprint(final_result)

if __name__ == '__main__':
    main()



