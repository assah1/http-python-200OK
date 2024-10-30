# Документация проекта Flask

## Описание

Данный проект представляет собой HTTP-сервер на Python с использованием Flask, который возвращает статус 200 OK на запрос к маршруту `/healthz`. Проект упакован в Docker-контейнер для упрощения развертывания и управления.

## Структура проекта
``
/project-root
│
├── app.py # Основной файл приложения
├── Dockerfile # Файл для сборки Docker-образа 
├── docker-compose.yaml # Файл конфигурации для Docker Compose 
├── requirements.txt # Зависимости проекта 
├── static # Директория для статических файлов 
│ └── style.css # CSS-стили для приложения 
└── templates # Директория для шаблонов HTML 
  └── index.html # Шаблон главной страницы
  ``

  ## Файлы и их назначения

- **`app.py`**: Основной код приложения.
- **`Dockerfile`**: Инструкции для сборки Docker-образа приложения.
- **`docker-compose.yaml`**: Был написан для удобства управление контейнерами без необходимости постоянного пробрасывания портов или проверки `docker ps` для понимания, на какой порт хоста выходит приложение.
- **`requirements.txt`**: Зависимости проекта, включая Flask.
- **`static/style.css`**: Статические файлы (CSS).
- **`templates/index.html`**: HTML-шаблон для главной страницы.
