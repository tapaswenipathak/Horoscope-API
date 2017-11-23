sunsigns = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
           "libra", "scorpio", "stagittarius", "capricorn", "aquarius", "pisces"]
timeframe = ["todays", "weekly", "yearly", "monthly"]
from pyhoroscope import Horoscope as horo

for sunsign in sunsigns:
    for j in timeframe:
        result = eval("horo.get_" + j + "_horoscope(sunsign)")
        print(result)
