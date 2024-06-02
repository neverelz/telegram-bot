import telebot
from telebot import types, TeleBot
import news
import config

# Создаем объект бота
bot = TeleBot(config.TOKEN)

# Список для хранения ID сообщений, отправленных ботом и пользователем
messages_to_delete = {}


# Функция для удаления всех сообщений в данном чате
def delete_all_messages(chat_id):
    if chat_id in messages_to_delete:
        for message_id in messages_to_delete[chat_id]:
            try:
                bot.delete_message(chat_id, message_id)
            except telebot.apihelper.ApiTelegramException as e:
                print(f"Не удалось удалить сообщение {message_id}: {e}")
        messages_to_delete[chat_id] = []



# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Фильмы", "Сериалы")
    markup.row("Мультфильмы", "Мультсериалы")
    return (markup)

# Меню выбора фильмов
def movies_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Киновселенная Marvel", "Звёздные войны")
    markup.row("Гарри Поттер", "Назад")
    markup.add(types.KeyboardButton("В главное меню"))
    return markup

# Меню выбора сериалов
def series_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Очень странные дела", "Игра престолов")
    markup.row("Сверхъественное", "Назад")
    markup.add(types.KeyboardButton("В главное меню"))
    return markup

# Меню выбора мультфильмов
def cartoons_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Гадкий Я и миньоны", "История игрушек")
    markup.row("Шрек", "Назад")
    markup.add(types.KeyboardButton("В главное меню"))
    return markup

# Меню выбора мультсериалов
def animated_series_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Гравити Фолз", "Три богатыря")
    markup.row("Симпсоны", "Назад")
    markup.add(types.KeyboardButton("В главное меню"))
    return markup

# Меню для категорий контента
def content_menu_marvel():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_starwars():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_harry_potter():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_osd():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_game_of_throns():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_supernatural():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_minion():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_toy_story():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_shrek():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_falls():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_3herros():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup
def content_menu_simpsons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Новости", "Обсуждения")
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup

# Меню для новостей Marvel
def news_menu_marvel():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Звёздные войны
def news_menu_starwars():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Гарри Поттер
def news_menu_harry_potter():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Очень странные дела
def news_menu_osd():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Игра престолов
def news_menu_game_of_throns():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Сверхъественное
def news_menu_supernatural():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Гадкий Я и миньоны
def news_menu_minion():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей История игрушек
def news_menu_toy_story():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Шрек
def news_menu_shrek():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Гравити Фолз
def news_menu_falls():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Три богатыря
def news_menu_3herros():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup
# Меню для новостей Симпсоны
def news_menu_simpsons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Назад", "В главное меню")
    return markup



# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in messages_to_delete:
        messages_to_delete[message.chat.id] = []
    msg = bot.send_message(message.chat.id, "Добро пожаловать! Выберите категорию:", reply_markup=main_menu())
    messages_to_delete[message.chat.id].append(message.message_id)  # Сохранить ID сообщения пользователя
    messages_to_delete[message.chat.id].append(msg.message_id)  # Сохранить ID сообщения бота




# Обработчик любых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global self
    self = "MAIN_MENU"

    if message.chat.id not in messages_to_delete:
        messages_to_delete[message.chat.id] = []
    messages_to_delete[message.chat.id].append(message.message_id)  # Сохранить ID сообщения пользователя

    if message.text == "Фильмы":
        msg = bot.send_message(message.chat.id, "Выберите категорию фильмов:", reply_markup=movies_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "MOVIE_MENU"
    elif message.text == "Сериалы":
        msg = bot.send_message(message.chat.id, "Выберите категорию сериалов:", reply_markup=series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SERIES_MENU"
    elif message.text == "Мультфильмы":
        msg = bot.send_message(message.chat.id, "Выберите категорию мультфильмов:", reply_markup=cartoons_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "CARTOON_MENU"
    elif message.text == "Мультсериалы":
        msg = bot.send_message(message.chat.id, "Выберите категорию мультсериалов:", reply_markup=animated_series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "CARTOON_SERIES_MENU"
    elif message.text == "Киновселенная Marvel":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Marvel", reply_markup=content_menu_marvel())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "MARVEL"
    elif self == "MARVEL" and message.text == "Новости":
        msg = bot.send_message(message.chat.id, news.generate_random_news_marvel())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Звёздные войны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Звёздных войн", reply_markup=content_menu_starwars())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "WARS"
    elif self == "WARS" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_starwars())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гарри Поттер":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гарри Поттера", reply_markup=content_menu_harry_potter())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "HP"
    elif self == "HP" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_hp())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Очень странные дела":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Очень странных дел", reply_markup=content_menu_osd())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "OSD"
    elif self == "OSD" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_osd())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Игра пристолов":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Игры пристолов", reply_markup=content_menu_game_of_throns())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "GAME_OF_THRONES"
    elif self == "GAME_OF_THRONES" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_game_of_thrones())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Сверхъественное":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Сверхъестественного", reply_markup=content_menu_supernatural())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SUPERNATURAL"
    elif self == "SUPERNATURAL" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_supernatural())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гадкий Я и миньоны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гадкого Я и миньонов", reply_markup=content_menu_minion())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "MINION"
    elif self == "MINION" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_minion())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "История игрушек":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Истории игрущек", reply_markup=content_menu_toy_story())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "TOY_SORT"
    elif self == "TOY_STORY" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_toy_story())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Шрек":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Шрека", reply_markup=content_menu_shrek())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SHREK"
    elif self == "SHREK" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_shrek())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гравити Фолз":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гравити Фолз", reply_markup=content_menu_falls())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "FALLS"
    elif self == "FALLS" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_falls())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Три богатыря":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Три богатыря", reply_markup=content_menu_3herros())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "HERROES"
    elif self == "HERROES" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_herros())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Симпсоны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Симпсонов", reply_markup=content_menu_simpsons())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SIMPSONS"
    elif self == "SIMPSONS" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_simpsons())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Обсуждения":
        msg = bot.send_message(message.chat.id, "Здесь пока нет обсуждений, но скоро появятся")
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "В главное меню":
        delete_all_messages(message.chat.id)
        msg = bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=main_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("MARVEL", "WARS", "HP"):
        self = "MOVIE_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора фильмов", reply_markup=movies_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("OSD", "GAME_OF_THRONES", "SUPERNATURAL"):
        self = "SERIES_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("MINION", "TOY_STORY", "SHREK"):
        self = "CARTOON_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=cartoons_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("FALLS", "HERROES", "SIMPSONS"):
        self = "CARTOON_SERIES_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=animated_series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("MOVIE_MENU", "SERIES_MENU", "CARTOON_MENU", "CARTOON_SERIES_MENU"):
        self = "MAIN_MENU"
        delete_all_messages(message.chat.id)
        msg = bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=main_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    else:
        msg = bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов меню.")
        messages_to_delete[message.chat.id].append(msg.message_id)






# def handle_input(self, input, message):
#     if self.state == "MAIN_MENU":
#         if input in ["Фильмы"]:
#             self.state = "MOVIE_MENU"
#         elif input in ["Сериалы"]:
#             self.state = "SERIES_MENU"
#         elif input in ["Мультфильмы"]:
#             self.state = "CARTOON_MENU"
#         elif input in ["Мультсериалы"]:
#             self.state = "CARTOON_SERIES_MENU"
#
#     elif self.state in ["MOVIE_MENU", "SERIES_MENU", "CARTOON_MENU", "CARTOON_SERIES_MENU"]:
#         if input == "Киновселенная Marvel":
#             self.state = "MARVEL"
#         elif input == "Новости" and self.state == "MARVEL":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_marvel())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Звёздные войны":
#             self.state = "WARS"
#         elif input == "Новости" and self.state == "WARS":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_starwars())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Гарри Поттер":
#             self.state = "HP"
#         elif input == "Новости" and self.state == "HP":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_hp())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Очень странные дела":
#             self.state = "OSD"
#         elif input == "Новости" and self.state == "OSD":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_osd())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Игра престолов":
#             self.state = "GAME_OF_THRONES"
#         elif input == "Новости" and self.state == "GAME_OF_THRONES":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_game_of_thrones())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Сверхъественное":
#             self.state = "SUPERNATURAL"
#         elif input == "Новости" and self.state == "SUPERNATURAL":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_supernatural())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Гадкий Я и миньоны":
#             self.state = "MINION"
#         elif input == "Новости" and self.state == "MINION":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_minion())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "История игрушек":
#             self.state = "TOY_STORY"
#         elif input == "Новости" and self.state == "TOY_STORY":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_toy_story())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Шрек":
#             self.state = "SHREK"
#         elif input == "Новости" and self.state == "SHREK":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_shrek())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Гравити Фолз":
#             self.state = "FALLS"
#         elif input == "Новости" and self.state == "FALLS":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_falls())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Три богатыря":
#             self.state = "HERROES"
#         elif input == "Новости" and self.state == "HERROES":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_herros())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Симпсоны":
#             self.state = "SIMPSONS"
#         elif input == "Новости" and self.state == "SIMPSONS":
#             for i in range (5):
#                 msg = bot.send_message(message.chat.id, news.generate_random_news_simpsons())
#                 messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Обсуждения":
#             return "Здесь пока нет обсуждений, но скоро появятся"
#
#
#         elif input == "Назад" and self.state in ("MARVEL", "WARS", "HP"):
#             self.state = "MOVIE_MENU"
#             msg = bot.send_message(message.chat.id, "Вы в меню выбора фильмов", reply_markup=movies_menu())
#             messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Назад" and self.state in ("OSD", "GAME_OF_THRONES", "SUPERNATURAL"):
#             self.state = "SERIES_MENU"
#             msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=series_menu())
#             messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Назад" and self.state in ("MINION", "TOY_STORY", "SHREK"):
#             self.state = "CARTOON_MENU"
#             msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=cartoons_menu())
#             messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Назад" and self.state in ("FALLS", "HERROES", "SIMPSONS"):
#             self.state = "CARTOON_SERIES_MENU"
#             msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=animated_series_menu())
#             messages_to_delete[message.chat.id].append(msg.message_id)
#         elif input == "Назад" and self.state in ("MOVIE_MENU", "SERIES_MENU", "CARTOON_MENU", "CARTOON_SERIES_MENU"):
#             self.state = "MAIN_MENU"
#             delete_all_messages(message.chat.id)
#             msg = bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=main_menu())
#             messages_to_delete[message.chat.id].append(msg.message_id)
#         else:
#             self.state = "MAIN_MENU"
#
#     return self.state



# Запуск бота
bot.polling()