# Проект "Веб-сервис СбощикВопросов"
**Задачи:**

1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
2. Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;
После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация: 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

## Структура проекта
<img width="812" alt="Снимок экрана 2023-10-17 в 20 53 50" src="https://github.com/radiant2958/QuestionService/assets/103328018/a3f06823-3249-4666-ab76-3f3292deec25">

- app: Главная директория приложения.
  - api: Основной модуль FastAPI приложения.
    - __ init __.py: Инициализационный файл для папки api.
    - questions.py: Содержит маршруты и логику, связанные с вопросами.
  - __ init __.py: Инициализационный файл для основной папки app.
  - main.py: Главный файл приложения, инициализация и запуск веб-сервера.
  - db: Каталог для доступа к базе данных.
    - __ init __.py: Инициализационный файл для db.
    - base.py: Базовая декларация для базы данных.
    - models.py: Определения моделей базы данных.
    - session.py: Создание и конфигурация сессии для базы данных.
- gitignore: Указывает, какие файлы или папки следует игнорировать в Git.
- Dockerfile: Инструкции для Docker по созданию образа приложения.
- README.md: Информация о проекте, инструкции и другие подробности.
- docker-compose.yml: Конфигурация для Docker Compose для многоконтейнерных приложений.
- requirements.txt: Список зависимостей Python для проекта.

## Инструкция по запуску веб-сервиса с использованием Docker

### Предварительные требования:
- Установленный **Docker**
- Установленный **docker-compose**

### Шаги для запуска:

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/radiant2958/QuestionService.git

   
2. **Переход в директорию проекта:**
   ```bash
   cd QuestionService

   
3. **Сборка и запуск контейнеров:**
    ```bash
    docker-compose up -d --build


4. **Тестирование сервиса:**
   
   После успешного запуска контейнеров веб-сервис будет доступен по адресу:
    ```bash
    http://localhost:8000

    
__Пример запроса сервису__
"<img width="1463" alt="Снимок экрана 2023-10-16 в 21 33 22" src="https://github.com/radiant2958/QuestionService/assets/103328018/3cac3c70-5358-4309-9773-4d6deca4818c">


5. **Проверка данных в базе данных:**
Чтобы проверить сохраненные данные в базе данных, выполните следующую команду:
    ```bash
    docker exec -it my_postgres psql -U anna mydatabase
После этого система запросит пароль. Введите пароль, указанный в вашем docker-compose файле (mail1234).


__Отображение сохраненных данных__
<img width="1128" alt="Снимок экрана 2023-10-16 в 21 34 39" src="https://github.com/radiant2958/QuestionService/assets/103328018/507f61df-7775-4796-bc85-15b32783463e">





