STOCK_NAME = "IBM"
APIKEY = "......."
NEWSAPIKEY = "......."
COMPANY_NAME = "Tesla"
EMAIL = "......@gmail.com"
PW = "......"

import requests
import datetime as dt
import smtplib

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
if month < 10:
    today = f"{year}-0{month}-{day}"
    yesterday = f"{year}-0{month}-{day-1}"
    dbyesterday = f"{year}-0{month}-{day - 2}"
else:
    today = f"{year}-{month}-{day}"
    yesterday = f"{year}-{month}-{day - 1}"
    dbyesterday = f"{year}-{month}-{day - 2}"

parameterStock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": APIKEY
}

parameterNews = {
    "qInTitle": COMPANY_NAME,
    "language": "en",
    "apiKey": NEWSAPIKEY
}

print(yesterday)
print(dbyesterday)

response = requests.get(STOCK_ENDPOINT, params=parameterStock)
# print(response.status_code)
yesterdayClose = round(float(response.json()["Time Series (Daily)"][yesterday]["4. close"]), 2)

dbyesterdayClose = round(float(response.json()["Time Series (Daily)"][dbyesterday]["4. close"]), 2)

percent = (round(((yesterdayClose-dbyesterdayClose)/dbyesterdayClose)*100, 2))

print(percent)
updown = None
if percent > 0:
    updown = "Up by"
else:
    updown = "Down by"
percent = abs(percent)

responsenews = requests.get(NEWS_ENDPOINT, params=parameterNews)
# print(responsenews.status_code)

top3Articles = responsenews.json()["articles"][:3]
print(top3Articles)

#LIST COMPREHENSION

formattedArticles = [f"{COMPANY_NAME} {updown} {percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in top3Articles]
#LIST COMPREHENSION

if percent > 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PW)
        for articles in formattedArticles:
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="testeremailforpython@yahoo.com",
                                msg=articles.encode('utf-8'))

#.encode for utf-8 was needed as ascii encoding was throwing some error to encode some particular character


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#1. - Get yesterday's closing stock price.
#2. - Get the day before yesterday's closing stock price

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"),get the first 3 news pieces for the COMPANY_NAME.

#6. -  use the News API to get articles related to the COMPANY_NAME.

#7. - Use Python slice operator to create a list that contains the first 3 articles.

#8. - Create a new list of the first 3 article's headline and description using list comprehension.
