""" for Twitter API v2 """

import jpholiday as jph
from datetime import date, datetime
import sys
import random
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
    # client.create_tweet(text=message)
    print(message)

def tweet_first(today: datetime, is_debug: bool = False) -> None:
    message = f"{generate_season_emoji(today=today)}\n{generate_first_day_emoji()}{today.month}月になりましたね。\n"
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
        message += "今月の祝日はありません。"
    
    tweet(message=message, is_debug=is_debug)

def tweet_holiday(today: datetime, is_debug: bool = False) -> None:
    holiday_name = jph.is_holiday_name(today)
    
    message = f"{generate_emoji()}今日は #{holiday_name} {generate_ending_of_word()}"
    tweet(message=message, is_debug=is_debug)

def generate_season_emoji(today: datetime) -> str:
    emojies = ( # 上から一月，二月，，，
        "🎍🌅🎉🔔<ｺﾞｰﾝ[あめましておめでとうございます]",
        "👹☃️",
        "🎎☀️",
        "😌🌸🌸🍡🍹",
        "🌤🎏",
        "☂️🐌",
        "🎆🎋⭐️🌠",
        "🐳☀️🎇🌻🏄🍉🍨🌴😎🐬",
        "🎑🎐🌕",
        "🎃👻💀",
        "🦃🍁🍂🍄",
        "🎄🎅🎁🎂🍗🔔<ｺﾞｰﾝ🍜👘"
    )
    return emojies[today.month-1]

def generate_first_day_emoji() -> str:
    return random_generator("🗓", "📅", "📝", "😀", "☀️")
    random_num = random.randint(0,4)

def generate_emoji() -> str:
    return random_generator("🎌", "👀", "😀", "㊗️", "☀️")

def generate_ending_of_word() -> str:
    return random_generator("です。", "です！", "だよ。", "！", "ですよー。")

def random_generator(*args) -> str:
    random_num = random.randint(0,len(args)-1)
    return args[random_num]

def main() -> None:
    # today = datetime.now()
    today = datetime(2022,12,31)

    is_debug = len(sys.argv) > 1
    
    if today.day == 1:
        tweet_first(today=today, is_debug=is_debug)
    if jph.is_holiday(today):
        tweet_holiday(today=today, is_debug=is_debug)

if __name__ == "__main__":
    main()