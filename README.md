# Выпускной проект

В качестве выпускного проекта, необходимо разработать Discord бота. Основная идея бота, бот ассистент, с возможностью рисовать изображения, силами искусственного интеллекта.
## Инструкция по запуску проекта
---
Для запуска проект существует несколько путей:
1. Запуск из исходного кода
2. Запуск докер контейнера

Ниже будут рассмотрены оба варианта запуска, с последовательностью необходимых команд, для успешного запуска бота.
### Запуск из исходного кода

Необходимо скачать [Python](https://www.python.org/downloads/release/python-31011/)

После установки python, необходимо клонировать репозиторий
```
git clone https://github.com/DevLn737/bot-project.git
cd ./bot-project
```

Создаём и активируем виртуальное окружение (Может отличаться в разных OS)
```
python3 -m venv venv
venv/Scripts/activate
```

В самом проекте выполнить установку зависимостей 
```
pip install -r requirements.txt
```

Бот использует переменные среды, которые подгружает из файла .env, на данный момент, необходим только Secret token бота, необходимо создать .env файл и заполнить его
```
SECRET_TOKEN=your_bot_token
```

После этого, бот можно запускать из корня директории с помощью команды
```
python3 bot.py
```

### Запуск docker контейнера

Первое что необходимо сделать, это установить [Docker Engine](https://docs.docker.com/engine/install/)

Скачиваем образ из docker hub
```
docker pull devln/discordbot:1.0.0
```

Запускаем контейнер
Где --name название контейнера SECRET_TOKEN="token" вместо token необходимо вставить свой секретный токен бота
```
docker run -d --name="container_name" -e SECRET_TOKEN="token" devln/discordbot:1.0.0
```
Ссылки
---

Dockerhub: <https://hub.docker.com/r/devln/discordbot>

GitHub: <https://github.com/DevLn737/bot-project>

Пригласить бота: <https://discord.com/oauth2/authorize?client_id=1241075954219094116>