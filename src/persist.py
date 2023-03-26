import re


class Persister:
    def __init__(self, logger=None) -> None:
        self.logger = logger

    def persist(self, data, output, delimiter="\t", newline="\n") -> None:
        clean = re.compile(r"[\t\r\n]")
        output.write("make" + delimiter + "model" + delimiter + "specs" + newline)  # header
        for make in data:
            for model in data[make]:
                for spec in data[make][model]:
                    output.write(clean.sub("", make) + delimiter + clean.sub("", model) + delimiter + clean.sub("", spec) + newline)  # row of data
