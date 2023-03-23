import os
import time
from datetime import datetime
import re

import requests

import utils


# def pull(url, retries=40, sleep_seconds=0.2):
#     utils.logger.info(f"GET {url}")

#     while retries > 0:
#         try:
#             time.sleep(sleep_seconds)
#             response = requests.get(url)
#             break
#         except ConnectionError:
#             retries = retries - 1
#             utils.logger.warn(f"Connection error {url}, retries {retries}.")
#             if retries <= 0:
#                 utils.logger.error(f"GET Failed. {url}")
#                 return ""
        
#     return response.content


# def parse_makes(url):
#     result = []
#     TARGET0 = b"<a class=\"megamenu-in-page__link\" href=\""
#     TARGET1 = b"\">"

#     utils.logger.debug("Parsing makes.")
#     hypertext = pull(url)
#     try:
#         while True:
#             idx = hypertext.index(TARGET0) + len(TARGET0)
#             hypertext = hypertext[idx:]
#             idx = hypertext.index(TARGET1)
#             result.append(hypertext[:idx].decode("utf-8"))
#             hypertext = hypertext[idx:]
#     except ValueError:
#         if result == []:
#             utils.logger.error(f"No makes scraped. {url}")

#     utils.logger.debug("Finished parsing makes.")
#     return result


# def parse_models(url):
#     result = []
#     TARGET0 = b"<a class=\"text-uppercase link link--blue\" href=\""
#     TARGET1 = b"\">"

#     utils.logger.debug("Parsing models.")
#     hypertext = pull(url)
#     try:
#         while True:
#             idx = hypertext.index(TARGET0) + len(TARGET0)
#             hypertext = hypertext[idx:]
#             idx = hypertext.index(TARGET1)
#             result.append(hypertext[:idx].decode("utf-8"))
#             hypertext = hypertext[idx:]
#     except ValueError:
#         if result == []:
#             utils.logger.error(f"No models scraped. {url}")

#     utils.logger.debug("Parsed models.")
#     return result


# def parse_specs(url):
#     SEPARATOR = ":"
#     result = []
#     TARGET0 = b"<div class=\"stats__list__accordion__body__stat__top__title\">"
#     TARGET1 = b"</div>"
#     TARGET2 = b"class=\"stats__list__accordion__body__stat__top__right__stat-time\">"
#     TARGET3 = b" <span"

#     utils.logger.debug("Parsing specs.")
#     hypertext = pull(url)
#     try:
#         while True:
#             data = ""
#             idx = hypertext.index(TARGET0) + len(TARGET0)
#             hypertext = hypertext[idx:]
#             idx = hypertext.index(TARGET1)
#             data += hypertext[:idx].decode("utf-8").strip()
#             hypertext = hypertext[idx:]
            
#             data += SEPARATOR

#             idx = hypertext.index(TARGET2) + len(TARGET2)
#             hypertext = hypertext[idx:]
#             idx = hypertext.index(TARGET3)
#             data += hypertext[:idx].decode("utf-8")

#             result.append(data)
#     except ValueError:
#         if result == []:
#             utils.logger.error(f"No specs scraped. {url}")

#     utils.logger.debug("Parsed specs.")
#     return result


# def persist(data):
#     DELIMITER = "\t"
#     NEWLINE = "\n"
#     REG = re.compile(r"([\t\r\n])")
#     DATA_DIR = os.path.abspath("../data")
#     FILENAME = f"{datetime.now().strftime('%Y-%m-%d_%Hhr_%Mmin')}_ptw_data.tsv"
    
#     utils.logger.info(f"Writing to file {FILENAME}.")
#     with open(DATA_DIR+FILENAME, "w") as f:
#         f.write("make" + DELIMITER + "model" + DELIMITER + "specs" + NEWLINE)  # header
#         for make in data:
#             for model in data[make]:
#                 for spec in data[make][model]:
#                     f.write(REG.sub("", make) + DELIMITER + REG.sub("", model) + DELIMITER + REG.sub("", spec) + NEWLINE)  # row of data
#     utils.logger.info("Finished writing to file.")


# def bootstrap(root_url):
#     makes = parse_makes(root_url)
#     data = dict.fromkeys(makes)
#     for make in makes:
#         models = parse_models(root_url+make)
#         data[make] = dict.fromkeys(models)
#         for model in models:
#             specs = parse_specs(root_url+model)
#             data[make][model] = specs
#     try:
#         persist(data)
#     except OSError as err:
#         utils.logger.critical(f"Error persisting to file. {err}")


if __name__ == "__main__":
    URL = "https://www.powertoweight.com/"
    start = datetime.now()
    utils.logger.info(f"Scrape start at {start}.")
    # bootstrap(URL)
    makes = parse_makes(root_url)
    data = dict.fromkeys(makes)
    for make in makes:
        models = parse_models(root_url+make)
        data[make] = dict.fromkeys(models)
        for model in models:
            specs = parse_specs(root_url+model)
            data[make][model] = specs
    try:
        persist(data)
    except OSError as err:
        utils.logger.critical(f"Error persisting to file. {err}")
    utils.logger.info(f"Finished scraping at {datetime.now()}. Elapsed time {datetime.now()-start}.")
