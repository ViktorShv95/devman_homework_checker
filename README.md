# Чат-бот Devman

Бот для получения уведомлений о проверке заданий с сайта  [Dvmn.org](https://dvmn.org/modules/).

## Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей.

```
pip install -r requirements.txt
```

Параметры `AUTH_TOKEN`, `BOT_TOKEN` и `CHAT_ID` должны находится в файле `.env` рядом со скриптом.

`AUTH_TOKEN` можно узнать в личном кабинете на сайте [Dvmn.org](https://dvmn.org/modules/) на странице API.

`BOT_TOKEN` можно узнать у специального бота `@BotFather`.

`CHAT_ID` можно узнать у специального бота `@userinfobot`.

## Пример использования

```
python main.py
```