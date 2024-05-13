import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from m3_3_course import get_course
from m3_3_wiki import get_article
# pip freeze > requi.txt
# Offset — отвечает за то, с какого диалога мы начнём читать сообщения. По умолчанию 0, читаем все сообщения, не пропускаем. Если поставим 1, то будем читать все диалоги кроме первого.
# Count — число ответов, которое может получить бот при одном запросе. 20 минимум, максимум 200.
# filter — какие диалоги мы читаем. (all — все, unread — непрочитанные, important — важные, unanswered — непрочитанные только для сообществ.).
"""
Архитектура longpolling

Long Polling — это технология, которая позволяет получать данные о новых событиях с помощью «длинных запросов». Сервер получает запрос, но отправляет ответ на него не сразу, а лишь тогда, когда произойдёт какое-либо событие (например, придёт новое сообщение), либо истечёт заданное время ожидания.
Если кто-то смотрел Шрека 3, когда они ехали в Тридевятое Королевство или Далёкое-Далёкое Королевство, осёл каждый 5 секунду спрашивает «мы приехали?», таким образом работает while true, Long Polling же работает другим образом. Он отправляет запрос на сервер и ждёт ответа, как только приходит ответ, у нас сразу срабатывает событие MESSAGE_NEW.

Подключение википедии

import wikipedia
def get_wiki_article(article):
    wikipedia.set_lang('ru')
    try:
        return wikipedia.summary(article)
    except wikipedia.WikipediaException:
        return('cannot find any')

Мы создали функцию get_wiki_article, которая принимает один аргумент – article.
Эту функцию мы будем вызывать внутри нашего бота. Внутри функции первой строчкой идёт установление языка запроса (set_lang). Далее конструкция try – except. Дело в том, что если такой статьи не будет – нам выкинет ошибку, но в таком случае бот просто упадёт, поэтому нужно это обработать. Внутри блока try мы прописали wikipedia.summary(article). Эта функция позволяет вывести первый абзац википедии по данному запросу.

Удаленный сервер
Удаленный сервер – это постоянно работающий компьютер (чаще всего без графического интерфейса), на котором работают различные приложения. Как правило, на удаленных серверах используется семейство ОС Linux. Удаленный сервер позволяет нашей программе работать 24/7, в то время когда наш компьютер может отдыхать. На сегодняшний день абсолютно все сервисы которыми мы с вами пользуемся, например, ВК, Телеграмм и тд – все находится на удаленных серверах. Настройка удаленного сервера – дело не из простых, для этого даже придумали специальную профессию – системный администратор.

Зависимости проекта
Зависимости – это набор библиотек и их версий, которые прямо или косвенно влияют на работу нашего проекта. Проект зависит от версий тех или иных библиотек. Обычно создают текстовый файлик и называют его requirements.txt, туда вписывают версии библиотек, которые используются в проекте.
Команды для работы с консолью в терминале на сайте:
ls – покажет что у вас находится в текущем каталоге
cd bot – перейти в папку bot
pip install – r –requirements.txt – установка необходимых библиотек
python vk_bot.py – запуск бота

"""
'''
Экcпорт библиотек
pip freeze > requi.txt

на хостинге в папке
pip install -r requi.txt
запуск
python имя_айла
'''
# sleshworld

# token="vk1.a.wscBb_H3kkvzmWarLzc4DDvJI9KWLCAbY_2xzpRko4S9APwx3QQt9NCT2zhiCQRXr0kGd2gdAjGJ9QRUWBuE2fLLfc7FCCv8MoKVv-WgljRIKXn3VYJRVF7F01y-dhVzGV3PmXMj9Ebb9SLnqkeR_sJ9ilY2do472yw4Ql4JsTzci-Oery2Pm3zhbpzYlptUQaled_jHmEmF-ttVOXDbqA"
token="vk1.a.XcDm5XYZjoI-zEcqzgQDb-BsLm8YHNcIn9Ts5teQ_8GR0QwMiuuh8qz-JkaVOZDL1Gu50Wk2xMXYf8vUJ5iW7Ob6LR4ySK3jlkQyLFgslLOSWNRf0dPMrsEknCXfmEKZ38RpwEivUr92bAz5e1NynHvGohGxscNroyyQpzuDn0uAcStm0HkZXrA3ejQiU28VRP3hR-hQHx7Ey0-JJHlXpw"

# https://www.pythonanywhere.com/

vk_session=vk_api.VkApi(token=token)
vk=vk_session.get_api()
upload=vk_api.VkUpload(vk)
photo=upload.photo_messages("kit.jpg")

# формат медиа вложения {type}{owner_id}_{media}
attachment = f"{photo[0]['owner_id']}_{photo[0]['id']}"
longpoll=VkLongPoll(vk_session)
# ===

def main(): # хз не заработало
    """ Пример создания клавиатуры для отправки ботом """

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Белая кнопка', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_location_button()

    keyboard.add_line()
    # keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=74030368&aid=6222115")

    keyboard.add_line()
    # 219817126_457239056
    # from_id 228683221
    keyboard.add_vkapps_button(app_id=6979558,
                               owner_id=-228683221,
                               label="Отправить клавиатуру",
                               hash="sendKeyboard")


    vk.messages.send(
        peer_id=123456,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Пример клавиатуры'
    )
# ===

# раньше while True
# try:
for event in longpoll.listen():
    if event.type==VkEventType.MESSAGE_NEW and event.to_me:
        msg=event.text.lower()
        # print(
        #     event.from_user,
        #     event.from_chat,
        #     event.from_group,
        #     event.from_me,
        #     event.to_me,
        #     event.attachments,
        #     event.message_data,
        #     event.message_id,
        #     event.timestamp,
        #     event.peer_id,
        #     event.flags,
        #     event.extra,
        #     event.extra_values,
        #     event.type_id
        # )
        print('====',msg)
        user_id=event.user_id
        random_id=get_random_id()
        if msg=="hi":
            vk.messages.send(user_id=user_id,random_id=random_id,message="HI")

        elif msg=='-kk':
            responce = "{0} рублей за доллар\n{1} рублей за euro\n{2} рублей за rmb\n".format(
                get_course('R01235'),
                get_course('R01239'),
                get_course('R01375'),
            )
            vk.messages.send(user_id=user_id, random_id=random_id, message = responce)
        elif msg.startswith("-k"):
            cur_code = msg[2:]
            responce = get_course(cur_code)
            vk.messages.send(user_id=user_id, random_id=random_id, message = responce)
        elif msg=="cat":
            own='photo-219817126_457239042'
            vk.messages.send(user_id=user_id, random_id=random_id, attachment=own) # no attachment
            # vk.method("messages.send",{"user_id":user_id,"random_id":random_id, "message":"туплю...", "attachment":attachment})
            # kit.jpg
            print("photo"+attachment)
        elif msg.startswith("-w"):
            article = msg[2:]
            responce = get_article(article)
            vk.messages.send(user_id=user_id, random_id=random_id, message = responce)
        elif msg=="-b": # не получилось настроить.
            # https://github.com/python273/vk_api/blob/master/examples/keyboard.py
            # main()
            keyboard=VkKeyboard(one_time=True)
            keyboard.add_location_button(payload=None) # This type of button takes the entire width of the line
            keyboard.add_line()
            keyboard.add_button('some_btn',color=VkKeyboardColor.PRIMARY)

            print(keyboard.get_keyboard(),'????')
            """This is a chat bot feature, change this status in settings
             menage => messages=> bots =>> turn on bot abilities"""
            vk.messages.send(user_id=user_id, random_id=random_id,message='Пример клавиатуры',keyboard=keyboard.get_keyboard())
        elif msg=="music":
            owner_id=2001377134
            audio_id=43377134
            vk.messages.send(user_id=user_id, random_id=random_id, attachment=f"audio{owner_id}_{audio_id}")

        else:
            responce=f"try again"
            vk.messages.send(user_id=user_id,random_id=random_id,message=responce)
# except:
#     pass
# ===HW===
'''
1/ Измените код парсера валют таким образом,
что команда которая подаётся на вход имеет следующий вид:
-к “ВАЛЮТА” и далее он выдаёт курс соответствующей валюты.
2/ Задеплойте код на сервер ещё раз. В качестве ответа можно прислать скриншоты.
'''