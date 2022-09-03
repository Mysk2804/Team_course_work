import requests
import configparser
from pprint import pprint
from chat_bot import Vk_bot

config = configparser.ConfigParser()
config.read("token.ini")

# -----------Класс который ищет по параметрам полученных с бота, так же принимает в себя токен api vk для поиска--------
class VK_users():
    def __init__(self, token, sex, city, age_from, age_to):
        self.token = token
        self.sex = sex
        self.city = city
        self.age_from = age_from
        self.age_to = age_to

    def info_vk_profiles(self):
        url = "https://api.vk.com/method/users.search"
        params = {
            'count': '20',
            'access_token': self.token,
            'v': '5.131',
            'id': '1',
            'city': '153',
            'sex': self.sex,
            'age_from': self.age_from,
            'age_to': self.age_to
        }
        new_url = requests.get(url, params=params)
        users = new_url.json()
        pprint(len(users['response']['items']))
        pprint(users)
        return users


if __name__ == '__main__':
    bot = Vk_bot()
    bot.start_chat_bot()
    lol = VK_users(config["Token"]["token1"], bot.sex, bot.city, bot.age_from, bot.age_to)
    lol.info_vk_profiles()