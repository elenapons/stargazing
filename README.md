# Star Gazing Mieres

Star Gazing Mieres is a simple app that helps you find the best days for stargazing in Mieres (Girona, Spain) over the next 7 days. Mieres is an excellent location for stargazing due to its minimal light pollution. This project was created as a learning exercise to improve my skills with Python and APIs.

## How does it work?

The app evaluates the stargazing conditions by considering two main factors: the moon cycle and the weather. These factors are crucial for determining the quality of stargazing on a given night.

To gather this information, the app uses [AEMET Open Data](https://opendata.aemet.es/centrodedescargas/inicio), which provides the weather forecast https://opendata.aemet.es/dist/index.html?

and the [pylunar library](https://pypi.org/project/pylunar/).

Based on these data, the app assigns one of the following ratings to each night:

* Perfect Night for Stargazing
* Very Good Night for Stargazing
* Good Night for Stargazing
* Another Night Would Be Better

These ratings help you plan your stargazing activities by indicating the nights with the most favorable conditions.

## Getting Started

To run the app, make sure you install the requirements.

$ python -m pip install -r requirements.txt

Now you can run the app.

$ python main.py