import os
from datetime import datetime

from definitions import PROJECT_ROOT
from src.utils.log import Logger
from src.parse import Parser
from src.persist import Persister
from src.remote import Remote

if __name__ == "__main__":
    ROOT_URL = "https://www.powertoweight.com/"
    
    CONFIG_FILENAME = "logger.conf"
    CONFIG_DIR = os.path.join(PROJECT_ROOT, os.path.join("config", CONFIG_FILENAME))

    # initialize logger
    Logger.initialize(CONFIG_DIR)
    
    rmote = Remote(Logger.log)  # find a better way to do this
    parser = Parser(rmote, Logger.log)
    persister = Persister(Logger.log)
    
    start = datetime.now()
    Logger.log.info(f"Scrape start at {start}.")

    makes = parser.parse_makes(ROOT_URL)
    data = dict.fromkeys(makes)
    for make in makes:
        models = parser.parse_models(ROOT_URL+make)
        data[make] = dict.fromkeys(models)
        for model in models:
            specs = parser.parse_specs(ROOT_URL+model)
            data[make][model] = specs

    DATA_DIR = os.path.join(PROJECT_ROOT, "data")
    FILENAME = f"{datetime.now().strftime('%Y-%m-%d_%Hhr_%Mmin')}_ptwr_data.tsv"
    FILEPATH = os.path.join(DATA_DIR, FILENAME)

    try:
        Logger.log.info(f"Writing to file {FILEPATH}.")
        with open(FILEPATH, 'w') as output:
            persister.persist(data, output)
            Logger.log.info("Finished writing to file.")
    except OSError as err:
            Logger.log.critical(f"Error persisting to file. {err}")


    Logger.log.info(f"Finished scraping at {datetime.now()}. Elapsed time {datetime.now()-start}.")
