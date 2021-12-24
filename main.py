import os
import time
import schedule
from dotenv import load_dotenv

from leetcode_parser import get_profile
from telegram_sender import send_message


def load_env_data():
    load_dotenv(".env")

    return {
        'users': os.getenv('USERS').split(','),
        'token': os.getenv('TOKEN'),
        'channel': os.getenv('CHANNEL')
    }


def prepare_message(profiles):
    text = "Hello Прогеры!!!\n" \
           "Сегодня {datetime}\n" \
        .format(
            datetime=time.strftime("%a, %d %b %Y %H:%M:%S")
        )
    max_total = 0
    max_point_user = ''
    for profile in profiles:
        if int(profile['total']) >= max_total:
            max_total = int(profile['total'])
            max_point_user = profile['username']
        # text += f"\n💜{profile['username']}💜" \
        #         f"\nRanking   🤑: {profile['ranking']}" \
        #         f"\nPoints   💲: {profile['points']}" \
        #         f"\nRealname   🛸: {profile['realName']}"  \
        #         f"\nTotal   🌠: {profile['total']}"   \
        #         f"\nEasy   🔨: {profile['easy']}"\
        #         f"\nMedium   ⚒: {profile['medium']}"\
        #         f"\nHard   ⚔️: {profile['hard']}" \
        #         "\n🐲🐲🐲" \
        #         "\n"

        text += f"\n💜{profile['username']}💜" \
                f"\nPoints   💲: {profile['points']}" \
                f"\nTotal   🌠: {profile['total']}" \
                f"\nEasy   🔨: {profile['easy']}" \
                "\n🐲🐲🐲" \
                "\n"
    text += f"\nToday's king is 🥇: {max_point_user}"

    text += f"\nДавайте, кодим дальше!"
    return text


def daily_informer():
    data = load_env_data()

    profiles = [get_profile(user) for user in data['users']]
    text = prepare_message(profiles)
    send_message(data['token'], data['channel'], text)




# schedule.every().day.at("08:00").do(daily_informer)
schedule.every().day.at("12:00").do(daily_informer)
schedule.every().day.at("15:00").do(daily_informer)
schedule.every().day.at("19:27").do(daily_informer)
schedule.every().day.at("21:00").do(daily_informer)
# schedule.every().day.at("23:00").do(daily_informer)

while True:
    schedule.run_pending()
    time.sleep(1)
