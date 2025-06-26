# Запуск проекта

python app.py

# Создание события

curl http://127.0.0.1:5000/api/v1/calendar/event/ -X POST -d "1|2025-06-26|header|event text"

# Просмотр всех событий

curl http://127.0.0.1:5000/api/v1/calendar/event/

# Просмотр события по идентификатору

curl http://127.0.0.1:5000/api/v1/calendar/event/1/

# Обновление события по идентификатору

curl http://127.0.0.1:5000/api/v1/calendar/event/1/ -X PUT -d "1|2025-06-26|header|new event text"

# Удаление события по идентификатору

curl http://127.0.0.1:5000/api/v1/calendar/event/1/ -X DELETE
