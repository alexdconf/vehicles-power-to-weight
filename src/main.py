import os
from datetime import datetime

import utils
import parse
import persist
import remote

if __name__ == "__main__":
    ROOT_URL = "https://www.powertoweight.com/"
    DATA_DIR = os.path.abspath("../data/")
    FILENAME = f"{datetime.now().strftime('%Y-%m-%d_%Hhr_%Mmin')}_ptw_data.tsv"
    parser = parse.Parser(remote.pull)
    persister = persist.Persister(DATA_DIR, FILENAME)
    
    start = datetime.now()
    utils.logger.info(f"Scrape start at {start}.")

    makes = parser.parse_makes(ROOT_URL)
    data = dict.fromkeys(makes)
    for make in makes:
        models = parser.parse_models(ROOT_URL+make)
        data[make] = dict.fromkeys(models)
        for model in models:
            specs = parser.parse_specs(ROOT_URL+model)
            data[make][model] = specs
    persister.persist(data)

    utils.logger.info(f"Finished scraping at {datetime.now()}. Elapsed time {datetime.now()-start}.")
