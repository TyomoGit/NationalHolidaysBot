""" for Twitter API v2 """

import jpholiday as jph
from datetime import date, datetime
import sys
from pprint import pprint
import tweepy
import keys # token

def tweet(message: str = str(datetime.now()), is_debug: bool = False) -> None:
    client = tweepy.Client(
        consumer_key=keys.API_KEY,
        consumer_secret=keys.API_SECRET,
        access_token=keys.ACCESS_TOKEN,
        access_token_secret=keys.ACCESS_TOKEN_SECRET
    )
    if is_debug:
        message = "⚠️これは試験的なツイートです。以下の内容は正確でない場合があります。\n" + message

    # pprint(client.create_tweet(text=message))
    client.create_tweet(text=message)

def tweet_first(today: datetime, is_debug: bool = False) -> None:
    message = f"🗓{today.month}月になりましたね。\n"
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
    
    if counter > 0:
        message += f"祝日は{counter}日あります:\n" + message_body.replace(f"{str(today.year)}-", "").replace("-", "/")
    else:
        message += "今月の祝日はありません。🐌"
    
    tweet(message=message, is_debug=is_debug)

def tweet_holiday(today: datetime, is_debug: bool = False) -> None:
    holiday_name = jph.is_holiday_name(today)
    message = f"🎌今日は #{holiday_name} です。"
    tweet(message=message, is_debug=is_debug)

def main() -> None:
    today = datetime.now().date()
    # today = datetime(2022,6,1).date()

    is_debug = len(sys.argv) > 1
    
    if today.day == 1:
        tweet_first(today=today, is_debug=is_debug)
    if jph.is_holiday(today):
        tweet_holiday(today=today, is_debug=is_debug)

if __name__ == "__main__":
    main()