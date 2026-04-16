# Cell 2/5: MOEX Client & Contracts
import requests, time

class MoexClient:
    def __init__(self, cfg):
        self._cfg = cfg
        self._session = requests.Session()

    def get(self, url, params=None):
        for attempt in range(1, self._cfg.retry + 1):
            try:
                r = self._session.get(url, params=params, timeout=self._cfg.timeout)
                r.raise_for_status()
                return r
            except Exception as e:
                if attempt == self._cfg.retry: raise e
                time.sleep(1.5 * attempt)

def identify_contracts(client, cfg, today):
    # Logic to identify F0, F1, F2 from MOEX ISS
    return {}
