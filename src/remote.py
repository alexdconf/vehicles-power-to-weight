import time

import requests

import utils


def pull(url, retries=40, sleep_seconds=0.2):
    utils.logger.info(f"GET {url}")

    while retries > 0:
        try:
            time.sleep(sleep_seconds)
            response = requests.get(url)
            break
        except ConnectionError:
            retries = retries - 1
            utils.logger.warn(f"Connection error {url}, retries {retries}.")
            if retries <= 0:
                utils.logger.error(f"GET Failed. {url}")
                return ""
        
    return response.content
