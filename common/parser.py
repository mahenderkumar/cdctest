import ConfigParser
from os.path import dirname, join
from selenium.common.exceptions import NoSuchElementException


# for join the file path with current run dir
def path_join(filepath):
    filedir = dirname(__file__)
    return join(filedir, filepath)


# for reading the config file : pageObjects.ini
def common_parser(section, field, config_path='../../pageObjects.ini'):
    try:
        parser = ConfigParser.ConfigParser()
        parser.read(path_join(config_path))
        if parser.has_section(section):
            if parser.has_option(section, field):
                return parser.get(section, field)
            else:
                return "Error: %s not found" % field
        else:
            return "Error: %s not found" % section
    except Exception, err:
        print Exception, err

def check(xpath,driver):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


if __name__ == "__main__":

    print common_parser('navbar', 'url')

