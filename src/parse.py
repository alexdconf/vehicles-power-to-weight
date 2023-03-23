import utils
from remote import pull


def parse_makes(url):
    result = []
    TARGET0 = b"<a class=\"megamenu-in-page__link\" href=\""
    TARGET1 = b"\">"

    utils.logger.debug("Parsing makes.")
    hypertext = pull(url)
    try:
        while True:
            idx = hypertext.index(TARGET0) + len(TARGET0)
            hypertext = hypertext[idx:]
            idx = hypertext.index(TARGET1)
            result.append(hypertext[:idx].decode("utf-8"))
            hypertext = hypertext[idx:]
    except ValueError:
        if result == []:
            utils.logger.error(f"No makes scraped. {url}")

    utils.logger.debug("Finished parsing makes.")
    return result


def parse_models(url):
    result = []
    TARGET0 = b"<a class=\"text-uppercase link link--blue\" href=\""
    TARGET1 = b"\">"

    utils.logger.debug("Parsing models.")
    hypertext = pull(url)
    try:
        while True:
            idx = hypertext.index(TARGET0) + len(TARGET0)
            hypertext = hypertext[idx:]
            idx = hypertext.index(TARGET1)
            result.append(hypertext[:idx].decode("utf-8"))
            hypertext = hypertext[idx:]
    except ValueError:
        if result == []:
            utils.logger.error(f"No models scraped. {url}")

    utils.logger.debug("Parsed models.")
    return result


def parse_specs(url):
    SEPARATOR = ":"
    result = []
    TARGET0 = b"<div class=\"stats__list__accordion__body__stat__top__title\">"
    TARGET1 = b"</div>"
    TARGET2 = b"class=\"stats__list__accordion__body__stat__top__right__stat-time\">"
    TARGET3 = b" <span"

    utils.logger.debug("Parsing specs.")
    hypertext = pull(url)
    try:
        while True:
            data = ""
            idx = hypertext.index(TARGET0) + len(TARGET0)
            hypertext = hypertext[idx:]
            idx = hypertext.index(TARGET1)
            data += hypertext[:idx].decode("utf-8").strip()
            hypertext = hypertext[idx:]
            
            data += SEPARATOR

            idx = hypertext.index(TARGET2) + len(TARGET2)
            hypertext = hypertext[idx:]
            idx = hypertext.index(TARGET3)
            data += hypertext[:idx].decode("utf-8")

            result.append(data)
    except ValueError:
        if result == []:
            utils.logger.error(f"No specs scraped. {url}")

    utils.logger.debug("Parsed specs.")
    return result
