import os
import re
from datetime import datetime

import utils

def persist(data):
    DELIMITER = "\t"
    NEWLINE = "\n"
    REG = re.compile(r"([\t\r\n])")
    DATA_DIR = os.path.abspath("../data")
    FILENAME = f"{datetime.now().strftime('%Y-%m-%d_%Hhr_%Mmin')}_ptw_data.tsv"
    
    utils.logger.info(f"Writing to file {FILENAME}.")
    with open(DATA_DIR+FILENAME, "w") as f:
        f.write("make" + DELIMITER + "model" + DELIMITER + "specs" + NEWLINE)  # header
        for make in data:
            for model in data[make]:
                for spec in data[make][model]:
                    f.write(REG.sub("", make) + DELIMITER + REG.sub("", model) + DELIMITER + REG.sub("", spec) + NEWLINE)  # row of data
    utils.logger.info("Finished writing to file.")
