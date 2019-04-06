import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

token="048e9cb9ad3f8ef871a788fb1e91a34b8c4ca9bb089e25d3b9d392256adaac591fb554a489a78c5b8b5d0"

vk=vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

random_id = 0

def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":random_id})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            print(request)
            random_id+=1
            if (request == "+"):
                print(event.user_id)
                write_msg(event.user_id, "Введите номер своего счетчика", random_id)
                if (request=="01"):
                    write_msg(event.user_id, "Что вам необходимо? \n 1) Текущие задания \n 2) Колличество токенов на вашем счету", random_id)
                    if (request == "1"):
                        write_msg(event.user_id, "Уменьшите потребление электроэнергии на ххх", random_id)
                    if (request == "2"):
                        write_msg(event.user_id, "Ваш счет = ххх", random_id)
                else:(print("Неверный номер счетчка"))