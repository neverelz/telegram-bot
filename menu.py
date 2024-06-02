from telebot import types


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


def chat_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("В главное меню"))
    return markup