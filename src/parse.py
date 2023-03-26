class Parser:
    def __init__(self, remote, logger=None) -> None:
        self.remote = remote
        self.logger = logger

    def _stepover(self, hypertext, target0, target1):
        idx = hypertext.index(target0) + len(target0)
        hypertext = hypertext[idx:]
        idx = hypertext.index(target1)
        data = hypertext[:idx]
        hypertext = hypertext[idx:]
        return data, hypertext

    def parse_makes(self, url):
        result = []
        TARGET0 = "<a class=\"megamenu-in-page__link\" href=\""
        TARGET1 = "\">"

        self.logger.debug("Parsing makes.") if self.logger is not None else None
        hypertext = self.remote.pull(url)
        try:
            while True:
                data, hypertext = self._stepover(hypertext, TARGET0, TARGET1)
                result.append(data)
        except ValueError:
            if result == []:
                self.logger.warn(f"No makes scraped. {url}") if self.logger is not None else None

        self.logger.debug("Finished parsing makes.") if self.logger is not None else None
        return result

    def parse_models(self, url):
        result = []
        TARGET0 = "<a class=\"text-uppercase link link--blue\" href=\""
        TARGET1 = "\">"

        self.logger.debug("Parsing models.") if self.logger is not None else None
        hypertext = self.remote.pull(url)
        try:
            while True:
                data, hypertext = self._stepover(hypertext, TARGET0, TARGET1)
                result.append(data)
        except ValueError:
            if result == []:
                self.logger.warn(f"No models scraped. {url}") if self.logger is not None else None

        self.logger.debug("Parsed models.") if self.logger is not None else None
        return result

    def parse_specs(self, url):
        SEPARATOR = ":"
        result = []
        TARGET0 = "<div class=\"stats__list__accordion__body__stat__top__title\">"
        TARGET1 = "</div>"
        TARGET2 = "class=\"stats__list__accordion__body__stat__top__right__stat-time\">"
        TARGET3 = " <span"

        self.logger.debug("Parsing specs.") if self.logger is not None else None
        hypertext = self.remote.pull(url)
        try:
            while True:
                data0, hypertext = self._stepover(hypertext, TARGET0, TARGET1)
                data0 += SEPARATOR
                data1, hypertext = self._stepover(hypertext, TARGET2, TARGET3)
                result.append(data0+data1)
        except ValueError:
            if result == []:
                self.logger.warn(f"No specs scraped. {url}") if self.logger is not None else None

        self.logger.debug("Parsed specs.") if self.logger is not None else None
        return result
