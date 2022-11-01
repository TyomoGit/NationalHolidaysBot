""" for Twitter API v2 """

from email import message
import jpholiday as jph
from datetime import date, datetime
import sys
from pprint import pprint
import tweepy
import keys

def tweet(message: str = str(datetime.now())) -> None:
    client = tweepy.Client(
        consumer_key=keys.API_KEY,
        consumer_secret=keys.API_SECRET,
        access_token=keys.ACCESS_TOKEN,
        access_token_secret=keys.ACCESS_TOKEN_SECRET
    )
    if len(sys.argv) > 1:
        message = "⚠️これは試験的なツイートです。以下の内容は正確でない場合があります。\n" + message

    pprint(client.create_tweet(text=message))

def behavior_begining_of_month(today: datetime) -> None:
    message = f"🗓{today.month}月になりましたね。"
    message_body = ""
    holidays = jph.month_holidays(today.year, today.month)
    counter = 0

    for holiday in holidays:
        counter += 1
        for content in holiday:
            if type(content) is date:
                message_body += str(content) + ": "
            elif type(content) is str:
                message_body += content
        message_body += "\n"
    
    message += f"祝日は{counter}日あります:\n" + message_body.replace(f"{str(today.year)}-", "").replace("-", "/")
    tweet(message)

def behavior_first(today: datetime) -> None:
    holiday_name = jph.is_holiday_name(today)
    message = f"🎌今日は #{holiday_name} です。"
    tweet(message)

def main():
    today = datetime.now().date()
    # today = datetime(2023,1,9).date()
    
    if today.day == 1:
        behavior_begining_of_month(today)
    if jph.is_holiday(today):
        behavior_first(today)

if __name__ == "__main__":
    main()