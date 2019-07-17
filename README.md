![](https://img.shields.io/badge/-Horoscope%20API-blueviolet.svg)

Horoscope API
======
[![GitHub issues](https://img.shields.io/github/issues/tapaswenipathak/Horoscope-API.svg)](https://github.com/tapaswenipathak/Horoscope-API/issues)
[![GitHub forks](https://img.shields.io/github/forks/tapaswenipathak/Horoscope-API.svg)](https://github.com/tapaswenipathak/Horoscope-API/network)
[![GitHub stars](https://img.shields.io/github/stars/tapaswenipathak/Horoscope-API.svg)](https://github.com/tapaswenipathak/Horoscope-API/stargazers)
[![GitHub license](https://img.shields.io/github/license/tapaswenipathak/Horoscope-API.svg)](https://github.com/tapaswenipathak/Horoscope-API/blob/master/License.md)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/tapaswenipathak/Horoscope-API.svg?label=Horoscope-API&style=social)](https://twitter.com/intent/tweet?text=Horoscope%20API:&url=https%3A%2F%2Fgithub.com%2Ftapaswenipathak%2FHoroscope-API)

An API to extract horoscope.

Please try - https://horoscopesapi.com which has a commercial license and more features.

## Table of Contents

* [Features](#features)
* [Usage](#api-usage)
* [Todo](#todo)
* [Contributing](#contributing)

# Features

* Today's horoscope 
  * broken down into date, sunsign and horoscope.
* Weekly horoscope
  * broken down into week, sunsign and horoscope.
* Monthly horoscope
  * broken down into month, sunsign and horoscope.
* Yearly horoscope
  * broken down into year, sunsign and horoscope.

# API Usage
### API Base URL: `http://horoscope-api.herokuapp.com/`

Result :
```json
{
  "author": "Tapasweni Pathak", 
  "author_url": "http://tapasweni-pathak.github.io/", 
  "base_url": "horoscope-api.herokuapp.com", 
  "project_name": "Horoscope API", 
  "project_url": "http://tapasweni-pathak.github.io/Horoscope-API"
}
```

### GET: `/horoscope/today/<sunsign>`
#### Example
Example usage: `GET http://horoscope-api.herokuapp.com/horoscope/today/Libra`

Example result:
```json
{
  "date": "04-09-2014", 
  "horoscope": "It is very likely that you will arouse immense jealousy in others with your success and growth in business. Your business rivals may attempt to dent your credit worthiness in one way or the other. You may prefer to deal with them subtly rather than confront them openly, feels Ganesha.       Astro Profile  Uncover the real you, and see for yourself the cosmic map that Almighty has constructed for you. This specific arrangement of planets, the numbers and the stars at the time you were born makes you unique. Discover such aspects through the free Astro Profile report.      Get It Now!  ", 
  "sunsign": "libra"
}
```

### GET: `/horoscope/week/<sunsign>`
#### Example
Example usage: `GET http://horoscope-api.herokuapp.com/horoscope/week/libra`

Output (excerpt):
```json
{
  "horoscope": "  Be prepared to face a hectic week, says Ganesha. Things that were dormant shall now start gaining momentum. Your financial graph will gradually start going up. Things on both the personal and professional fronts are likely to become smoother. Your relations with your bosses shall improve. Boss and You! Finding difficulty to get along with your superior in your office, our expert astrologers can help you out. Get this report to get guidance from an astrological standpoint \u2013 as this report is based on your Natal Chart, it will be fully personalised for you. You shall be spending money on friends, but they shall return the favour by holding you in high regard and showering a lot of affection on you. This week, you shall also be able to earn through contacts and your reputation shall spread through word of mouth, fetching many assignments. This week is good for working with youngsters. That is to say, if you wish to impart training to the youngsters in your company or even in your family, this is the best week. Ganesha feels your approach towards social and personal issues shall be diplomatic.   Birth Horoscope Use the power of Astrology to understand yourself in a better way and get a sense of direction and purpose in life. The cosmic imprint of the stars has a profound impact on your life. Unravel your true potential through the Birth Horoscope report, being offered for free.      Get It Now! ", 
  "sunsign": "libra", 
  "week": "31-08-2014 \u2013 06-09-2014 "
}
```

### GET: `/horoscope/month/<sunsign>`
#### Example
Example usage: `GET http://horoscope-api.herokuapp.com/horoscope/month/libra`

Output (excerpt):
```json
{
  "horoscope": "  Ganesha says brace up for a hectic month, as every aspect of your life shall keep you extremely busy. On the work front, your relations with seniors shall improve. As for work, you shall easily complete the projects assigned to you. Your social network and contacts shall matter a lot this month. You may also quit your job and start a business, to improve your financial condition. However, don\u2019t take any hasty decisions, cautions Ganesha. You are likely to be tempted to take some drastic steps to improve your finances. However, you should consult experts before undertaking anything risky. Also, start saving and chart out your investment plans. Over the course of the month, your finances shall improve gradually. Gains through investments in business are also indicated. To get some valuable tips on how to improve your financial condition even more, try the Birth Chart based report Wealth Ask a Question Detailed. As per Ganesha, your personal life may be fairly smooth this month, provided you are flexible and accommodating. Planetary positions indicate that your stubbornness may negatively affect your spouse and other members of your family.  Shani Dosha  Shani Dosha occurs when Saturn, the feared, mighty planet, is debilitated or occupies any of the Cardinal Houses (1, 4, 7, 10) in Aries, Cancer, Leo, or Scorpio or is Retrograde or Combust (by Sun) in those Houses (whatever be the Sign, except Libra, Capricorn and Aquarius) in a Horoscope. These planetary positions can cause troubles for you. Find out and deal well!    Get It Now! ", 
  "month": "Sep 2014 ", 
  "sunsign": "libra"
}
```

### GET: `/horoscope/year/<sunsign>`
Example usage: `GET http://horoscope-api.herokuapp.com/horoscope/year/libra`
 Output (excerpt):
 ```json
 {
   "horoscope": "The planetary alignment indicate that you will have trouble controlling your temper during the year ahead. Be very careful of your words and actions as even petty issues may go out of hand in no time. As far as your love life is concerned, there will some ups and downs during year . Be unbiased and practical while sorting out issues with your beloved, else you will not be able to stop things from going bad to worse. This year, you need to be very clear about how you are going to handle your finances. According to Ganesha, you should pay special attention to your spendings and cash outflow. Whereas for your business, it may prove to be an excellent year. In all likelihood, you will come across lucrative business opportunities. The transiting Jupiter may bring you a favourable period on the career front in the form of a promotion or an increment. Well, be prepared to accept more responsibilities.",
   "sunsign": "libra",
   "year": "2014 "
}
```
# Todo
* Personality Profile
* Facts About a Sunsign
* Practical Side of a Sunsign
* Astrological Perspective of a Sunsign

# API Wrappers 
* [Java Wrapper](https://github.com/TheBotBox/Horoscope-API) by [TheBotBox](https://github.com/TheBotBox/) 
* [Flutter Wrapper](https://github.com/sumitgohil/flutter_horoscope) by [SumitGohil](https://github.com/sumitgohil/) 

# Contributing
Feel free to submit a pull request or an issue!



#### Note 1 : This parses [GaneshaSpeaks](http://www.ganeshaspeaks.com/) unofficialy.  

#### Note 2 : If the API goes down, please open a issue or comment on already existing one with the problem(s) that you are facing. This is the best way to let me know that the API is not working, avoid sending email. 

#### Note 3 : You can also try - https://horoscopesapi.com which has a commercial license and more features.

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/tapasweni-pathak/horoscope-api/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
