from lxml import html
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup

####################################################################
# API
####################################################################

class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        date = soup.find('p', class_='mb-0').text
        date_utc = datetime.now(timezone.utc)
        date_website = "-".join(date.split('-')[::-1])
        date_local = str(date_utc.astimezone()).split(' ')[0]

        if date_local < date_website :
            url = "https://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            horoscope = soup.find('p', id='horo_content').text

        elif date_local > date_website :
            url = "https://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            horoscope = soup.find('p', id='horo_content').text

        else :
            horoscope = soup.find('p', id='horo_content').text

        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        dict = {
            'date': date_local,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        week = soup.find('p', class_='mb-0').text
        horoscope = soup.find('p', id='horo_content').text
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            month = soup.find('p', class_='mb-0').text
            horoscope = soup.find('p', id='horo_content').text
            horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
            dict = {
                'month': month,
                'horoscope': horoscope,
                'sunsign': sunsign
            }
        except Exception as ex:
            if not month:
                month = 'Error: None'
            dict = {
                'year': month,
                'horoscope': 'Error: the source is broken!',
                'sunsign': sunsign
            }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            year = soup.find('p', class_='mb-0').text
            horoscope = soup.find('p', id='horo_content').text
            horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
            dict = {
                'year': year,
                'horoscope': horoscope,
                'sunsign': sunsign
            }
        except Exception as ex:
            if not year:
                year = 'Error: None'
            dict = {
                'year': year,
                'horoscope': 'Error: the source is broken!',
                'sunsign': sunsign
            }

        return dict

