# -*- coding: utf-8 -*-
import math
import requests


url = "https://data.nasa.gov/resource/gh4g-9sfh.json"
data = requests.get(url).json()