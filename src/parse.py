import utils


class Parser:
    def __init__(self, pull) -> None:
        self.pull = pull

    def stepover(self, hypertext, target0, target1):
        idx = hypertext.index(target0) + len(target0)
        hypertext = hypertext[idx:]
        idx = hypertext.index(target1)
        data = hypertext[:idx].decode("utf-8")
        hypertext = hypertext[idx:]
        return data, hypertext

    def parse_makes(self, url):
        result = []
        TARGET0 = b"<a class=\"megamenu-in-page__link\" href=\""
        TARGET1 = b"\">"

        utils.logger.debug("Parsing makes.")
        hypertext = self.pull(url)
        try:
            while True:
                data, hypertext = self.stepover(hypertext, TARGET0, TARGET1)
                result.append(data)
        except ValueError:
            if result == []:
                utils.logger.warn(f"No makes scraped. {url}")

        utils.logger.debug("Finished parsing makes.")
        return result

    def parse_models(self, url):
        result = []
        TARGET0 = b"<a class=\"text-uppercase link link--blue\" href=\""
        TARGET1 = b"\">"

        utils.logger.debug("Parsing models.")
        hypertext = self.pull(url)
        try:
            while True:
                data, hypertext = self.stepover(hypertext, TARGET0, TARGET1)
                result.append(data)
        except ValueError:
            if result == []:
                utils.logger.warn(f"No models scraped. {url}")

        utils.logger.debug("Parsed models.")
        return result

    def parse_specs(self, url):
        SEPARATOR = ":"
        result = []
        TARGET0 = b"<div class=\"stats__list__accordion__body__stat__top__title\">"
        TARGET1 = b"</div>"
        TARGET2 = b"class=\"stats__list__accordion__body__stat__top__right__stat-time\">"
        TARGET3 = b" <span"

        utils.logger.debug("Parsing specs.")
        hypertext = self.pull(url)
        try:
            while True:
                data0, hypertext = self.stepover(hypertext, TARGET0, TARGET1)
                data0 += SEPARATOR
                data1, hypertext = self.stepover(hypertext, TARGET2, TARGET3)
                result.append(data0+data1)
        except ValueError:
            if result == []:
                utils.logger.warn(f"No specs scraped. {url}")

        utils.logger.debug("Parsed specs.")
        return result
