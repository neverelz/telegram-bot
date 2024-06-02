import telebot
from telebot import TeleBot
import config
import news
import menu

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


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in messages_to_delete:
        messages_to_delete[message.chat.id] = []
    msg = bot.send_message(message.chat.id, "Добро пожаловать! Выберите категорию:", reply_markup=menu.main_menu())
    messages_to_delete[message.chat.id].append(message.message_id)  # Сохранить ID сообщения пользователя
    messages_to_delete[message.chat.id].append(msg.message_id)  # Сохранить ID сообщения бота


self = "MAIN_MENU"
# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):

    global self

    if message.chat.id not in messages_to_delete:
        messages_to_delete[message.chat.id] = []
    messages_to_delete[message.chat.id].append(message.message_id)  # Сохранить ID сообщения пользователя

    if message.text == "Фильмы":
        msg = bot.send_message(message.chat.id, "Выберите категорию фильмов:", reply_markup=menu.movies_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "MOVIE_MENU"
    elif message.text == "Сериалы":
        msg = bot.send_message(message.chat.id, "Выберите категорию сериалов:", reply_markup=menu.series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SERIES_MENU"
    elif message.text == "Мультфильмы":
        msg = bot.send_message(message.chat.id, "Выберите категорию мультфильмов:", reply_markup=menu.cartoons_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "CARTOON_MENU"
    elif message.text == "Мультсериалы":
        msg = bot.send_message(message.chat.id, "Выберите категорию мультсериалов:", reply_markup=menu.animated_series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "CARTOON_SERIES_MENU"
    elif message.text == "Киновселенная Marvel":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Marvel", reply_markup=menu.content_menu_marvel())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "MARVEL"
    elif self == "MARVEL" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_marvel())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Звёздные войны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Звёздных войн", reply_markup=menu.content_menu_starwars())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "WARS"
    elif self == "WARS" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_starwars())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гарри Поттер":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гарри Поттера", reply_markup=menu.content_menu_harry_potter())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "HP"
    elif self == "HP" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_hp())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Очень странные дела":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Очень странных дел", reply_markup=menu.content_menu_osd())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "OSD"
    elif self == "OSD" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_osd())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Игра пристолов":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Игры пристолов", reply_markup=menu.content_menu_game_of_throns())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "GAME_OF_THRONES"
    elif self == "GAME_OF_THRONES" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_game_of_thrones())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Сверхъественное":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Сверхъестественного", reply_markup=menu.content_menu_supernatural())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SUPERNATURAL"
    elif self == "SUPERNATURAL" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_supernatural())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гадкий Я и миньоны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гадкого Я и миньонов", reply_markup=menu.content_menu_minion())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "MINION"
    elif self == "MINION" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_minion())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "История игрушек":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Истории игрущек", reply_markup=menu.content_menu_toy_story())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "TOY_SORT"
    elif self == "TOY_STORY" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_toy_story())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Шрек":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Шрека", reply_markup=menu.content_menu_shrek())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SHREK"
    elif self == "SHREK" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_shrek())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Гравити Фолз":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Гравити Фолз", reply_markup=menu.content_menu_falls())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "FALLS"
    elif self == "FALLS" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_falls())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Три богатыря":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Три богатыря", reply_markup=menu.content_menu_3herros())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "HERROES"
    elif self == "HERROES" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_herros())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Симпсоны":
        msg = bot.send_message(message.chat.id, "Выбрана вселенная Симпсонов", reply_markup=menu.content_menu_simpsons())
        messages_to_delete[message.chat.id].append(msg.message_id)
        self = "SIMPSONS"
    elif self == "SIMPSONS" and message.text == "Новости":
        for i in range(5):
            msg = bot.send_message(message.chat.id, news.generate_random_news_simpsons())
            messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "В главное меню":
        delete_all_messages(message.chat.id)
        msg = bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=menu.main_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("MARVEL", "WARS", "HP"):
        self = "MOVIE_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора фильмов", reply_markup=menu.movies_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("OSD", "GAME_OF_THRONES", "SUPERNATURAL"):
        self = "SERIES_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=menu.series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("MINION", "TOY_STORY", "SHREK"):
        self = "CARTOON_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=menu.cartoons_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("FALLS", "HERROES", "SIMPSONS"):
        self = "CARTOON_SERIES_MENU"
        msg = bot.send_message(message.chat.id, "Вы в меню выбора сериалов", reply_markup=menu.animated_series_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Назад" and self in ("MOVIE_MENU", "SERIES_MENU", "CARTOON_MENU", "CARTOON_SERIES_MENU"):
        self = "MAIN_MENU"
        delete_all_messages(message.chat.id)
        msg = bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=menu.main_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
    elif message.text == "Обсуждения":
        msg = bot.send_message(message.chat.id, "Вы в разделе обсуждений", reply_markup=menu.chat_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)
        msg = bot.send_message(message.chat.id, "Здесь скоро появятся новые обсуждения", reply_markup=menu.chat_menu())
        messages_to_delete[message.chat.id].append(msg.message_id)


# Запуск бота
bot.polling()