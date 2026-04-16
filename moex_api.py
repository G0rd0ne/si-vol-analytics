# Cells: eVcfSVEFZJlh, lw7Cwpd3ZRFy
import requests
import pandas as pd
import logging

class MoexClient:
    def __init__(self, cfg):
        self._cfg = cfg
        self._session = requests.Session()