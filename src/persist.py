import os
import re

import utils


class Persister:
    def __init__(self, data_dir, filename, delimiter="\t", newline="\n") -> None:
        self.data_dir = data_dir
        self.filename = filename
        self.delimiter = delimiter
        self.newline = newline

    def persist(self, data):
        clean = re.compile(r"[\t\r\n]")
        utils.logger.info(f"Writing to file {self.filename}.")
        try:
            with open(os.path.join(self.data_dir+self.filename), "w") as f:
                f.write("make" + self.delimiter + "model" + self.delimiter + "specs" + self.newline)  # header
                for make in data:
                    for model in data[make]:
                        for spec in data[make][model]:
                            f.write(clean.sub("", make) + self.delimiter + clean.sub("", model) + self.delimiter + clean.sub("", spec) + self.newline)  # row of data
            utils.logger.info("Finished writing to file.")
        except OSError as err:
            utils.logger.critical(f"Error persisting to file. {err}")
