#Создаём имедж на основе имеджа ->
FROM python:3.9-alpine3.16

#Скопируем файл *.тхт в папку ->
COPY requirements.txt /temp/requirements.txt
#Копируем папку Service в корень Dosker контейнера
COPY service /service
#Обозначаем воркдир. При передаче комманд
#они будут запускаться в этой директории, уменьшит путь для рабочих фалов
WORKDIR /service
#Открываем порт. Внутри докера пробрасываем порт, чтобы иметь к нему доступ из основной системы
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt
#Создаст пользователя в ОС без пароля
RUN adduser --disabled-password service-user
#Чтобы комманды запускались не под рутом активируем ЮЗЕРА
USER service-user


