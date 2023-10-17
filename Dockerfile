# Используем базовый образ Python 3.8
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /Progect/app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости из файла requirements.txt
RUN pip install -r requirements.txt



# Копируем все файлы из текущей директории (включая ваш код) в рабочую директорию контейнера
COPY . .

# Экспонируем порт, на котором будет работать ваше FastAPI-приложение
EXPOSE 8000

# ENV PATH="/Progect/myenv/bin:${PATH}"
# Команда для запуска вашего FastAPI-приложения

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]