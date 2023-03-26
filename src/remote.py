import time

import requests


class Remote:
    def __init__(self, logger=None) -> None:
        self.get = requests.get
        self.logger = logger

    def pull(self, url, retries=40, sleep_seconds=0.2) -> str:
        self.logger.info(f"GET {url}") if self.logger is not None else None

        while retries > 0:
            try:
                time.sleep(sleep_seconds)
                response = self.get(url)
                break
            except ConnectionError:
                retries = retries - 1
                self.logger.warn(f"Connection error {url}, retries {retries}.") if self.logger is not None else None
                if retries <= 0:
                    self.logger.error(f"GET Failed. {url}") if self.logger is not None else None
                    return ""
            
        return str(response.content)
