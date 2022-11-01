""" for Twitter API v2 """

from email import message
import jpholiday as jph
from datetime import datetime
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
    pprint(client.create_tweet(text=message))

def main():
    today = datetime.now().date()

    if jph.is_holiday(today):
        holiday_name = jph.is_holiday_name(today)
        message = f"今日は{holiday_name}です。"
        # tweet(message)
    
    if today.day == 1:
        message = f"{today.month}月になりましたね。"
        message_holidays = ""
        holidays = jph.month_holidays(today.year, today.month)
        counter = 0

        for holiday in holidays:
            counter += 1
            for content in holiday:
                if type(content) is datetime:
                    message_holidays += str(content) + ": "
                elif type(content) is str:
                    message_holidays += content
            message_holidays += "\n"
        
        message += f"祝日は{counter}日あります:\n" + message_holidays
        tweet(message)

if __name__ == "__main__":
    main()