import urllib.request
from lxml import etree


####################################################################
# API
####################################################################

class Horoscope:
    def __init__(self):
        pass

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        html_parser = etree.HTMLParser()
        tree = etree.parse(response, html_parser)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("['", "").replace("']", "").replace("['(", "").replace(")']", "")

        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("[\"\\r\\n   ", "").replace("    \\r\\n    \\r\\n  \"]", "")
        horoscope = horoscope.strip()
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "https://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        html_parser = etree.HTMLParser()
        tree = etree.parse(response, html_parser)
        week = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        week = week.replace("['", "").replace("[u'\\n", "").replace("']", "").replace("\\u2013",
                                                                                      "-")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\r\\n   ", "").replace("     \\r\\n  ", "").replace(
            "    \\r\\n    \\r\\n  ", "").replace("['", "").replace("']", "")
        horoscope = horoscope.strip()
        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "https://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        html_parser = etree.HTMLParser()
        tree = etree.parse(response, html_parser)
        month = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        month = month.replace("['", "").replace("\\r\\n   ", "").replace("['\\n", "").replace("']",
                                                                                              "")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()[1]"))
        horoscope = horoscope.replace("\\r\\n   ", "").replace("['", "").replace("']", "")
        horoscope = horoscope.strip()
        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "https://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        html_parser = etree.HTMLParser()
        tree = etree.parse(response, html_parser)
        year = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        year = year.replace("['", "").replace("['\\n", "").replace("']", "")

        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("['\\r\\n   ", "").replace("    \\r\\n    \\r\\n  ",
                                                                 "").replace("[u'", "").replace(
            "']", "").replace("\\xe2\\x80\\x99s", "")
        horoscope = horoscope.strip()
        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
