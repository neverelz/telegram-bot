import telebot
from telebot import types
import news

# Создаем объект бота
API_TOKEN = '6510413056:AAHYeLyUgUGpMAwN6d7iRqof3mKdvPILd5Q'
bot = telebot.TeleBot(API_TOKEN)

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

    if message.chat.id not in messages_to_delete:
        messages_to_delete[message.chat.id] = []
    messages_to_delete[message.chat.id].append(message.message_id)  # Сохранить ID сообщения пользователя

    if message.text == "Фильмы":
        msg = bot.send_message(message.chat.id, "Выберите категорию фильмов:", reply_markup=movies_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Сериалы":
        msg = bot.send_message(message.chat.id, "Выберите категорию сериалов:", reply_markup=series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Мультфильмы":
        msg = bot.send_message(message.chat.id, "Выберите категорию мультфильмов:", reply_markup=cartoons_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Мультсериалы":
        msg = bot.send_message(message.chat.id, "Выберите категорию мультсериалов:", reply_markup=animated_series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Киновселенная Marvel":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Marvel", reply_markup=content_menu_marvel())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Звёздные войны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Звёздных войн", reply_markup=content_menu_starwars())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гарри Поттер":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гарри Поттера", reply_markup=content_menu_harry_potter())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Очень странные дела":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Очень странных дел", reply_markup=content_menu_osd())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Игра пристолов":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Игры пристолов", reply_markup=content_menu_game_of_throns())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Сверхъественное":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Сверхъестественного", reply_markup=content_menu_supernatural())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гадкий Я и миньоны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гадкого Я и миньонов", reply_markup=content_menu_minion())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "История игрушек":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Истории игрущек", reply_markup=content_menu_toy_story())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Шрек":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Шрека", reply_markup=content_menu_shrek())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гравити Фолз":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гравити Фолз", reply_markup=content_menu_falls())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Три богатыря":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Три богатыря", reply_markup=content_menu_3herros())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Симпсоны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Симпсонов", reply_markup=content_menu_simpsons())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Обсуждения":
        msg = bot.send_message(message.chat.id, "Здесь пока нет обсуждений, но скоро появятся")
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "В главное меню":
        delete_all_messages(message.chat.id)
        msg = bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=main_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    else:
        msg = bot.send_message(message.chat.id, "Пожалуйста, выберите один из вариантов меню.")
        messages_to_delete[message.chat.id].append(msg.message_id)

def __init__(self):
    self.state = "MAIN_MENU"

def handle_input(self, input, message):
    if self.state == "MAIN_MENU":
        if input in ["Киновселенная Marvel", "Звёздные войны", "Гарри Поттер"]:
            self.state = "MOVIE_MENU"
        elif input in ["Очень странные дела", "Игра престолов", "Сверхъественное"]:
            self.state = "SERIES_MENU"
        elif input in ["Гадкий Я и миньоны", "История игрушек", "Шрек"]:
            self.state = "CARTOON_MENU"
        elif input in ["Гравити Фолз", "Три богатыря", "Симпсоны"]:
            self.state = "CARTOON_SERIES_MENU"

    elif self.state in ["MOVIE_MENU", "SERIES_MENU", "CARTOON_MENU", "CARTOON_SERIES_MENU"]:
        if input == "Киновселенная Marvel":
            self.state = "MARVEL"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_marvel())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Звёздные войны":
            self.state = "WARS"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_starwars())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Гарри Поттер":
            self.state = "HP"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_hp())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Очень странные дела":
            self.state = "OSD"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_osd())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Игра престолов":
            self.state = "GAME_OF_THRONES"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_game_of_thrones())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Сверхъественное":
            self.state = "SUPERNATURAL"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_supernatural())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Гадкий Я и миньоны":
            self.state = "MINION"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_minion())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "История игрушек":
            self.state = "TOY_STORY"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_toy_story())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Шрек":
            self.state = "SHREK"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_shrek())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Гравити Фолз":
            self.state = "FALS"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_falls())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Три богатыря":
            self.state = "HERROES"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_herros())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Симпсоны":
            self.state = "SIMPSONS"
            if input == "Новости":
                for i in range (5):
                    msg = bot.send_message(message.chat.id, news.generate_random_news_simpsons())
                    messages_to_delete[message.chat.id].append(msg.message_id)
        elif input == "Обсуждения":
            return "Здесь пока нет обсуждений, но скоро появятся"
        elif input == "Назад":
            self.state = "MAIN_MENU"
        else:
            self.state = "MAIN_MENU"


    return self.state



# Запуск бота
bot.polling()