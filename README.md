[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub contributors](https://img.shields.io/github/contributors/Ornstein89/VTB_API_hack2022)

# LeadersOfDigital2021_FoxhoundTeam
Решение команды Foxhound в финале хакатона "Цифровой прорыв", 2-4 декабря 2021 г.

## Описание приложения

Решение команды Foxhound представляет собой сервис для подготовки персонала для управления БПЛА.

Здесь представлены три модуля: 
- Выполнение практических заданий в эмуляторе
- Тестирование
- Теоритические материалы

## Инструкция по запуску
Демо решение расположено по адресу [http://51.250.4.103/](http://51.250.4.103/) до 20:00 вечера 6 декабря 2021 г.

Логин: admin

Пароль: 1234

Для запуска локально, см. Развертывание через docker-compose

## Руководство пользователя
В интерфейсе присутствует три основных вкладки: Задания, Теоритические материалы и Тесты. 

Во вкладке "Задания" отображаются практические задания, которые будут выполнятся в симуляторе. 

Тут же администратор может редактировать и создавать новые задания. 

Для выполнения задач в симуляторе, необходимо скачать симулятор и клиент.

Во вкладке "Теоритические материалы" можно найти статьи для подготовки к тестированию и практическим заданиям. Тут же администратор может редактировать и создавать статьи. Статьи поддерживают разметку mardown.

Во вкладке "Тесты" пользователь может проходить тесты, которые помогут закрепить теоритические материалы перед переходом к практическим заданиям. Также присутсвует редактор тестов для адмнистратора.


## Развертывание через docker-compose
1. Установить [docker](https://docs.docker.com/engine/install/ubuntu/)
2. Установить [docker-compose](https://docs.docker.com/compose/install/)
3. В папке compose создать файлы .env и .backend.env и заполнить их в соответствии с примерами
4. Запустить команду docker-compose up -d с правами суперпользователя
```bash
sudo docker-compose up -d
```
5. Настроить внешний nginx, который будет пересылать все запросы на порт приложения
## Команды docker-compose 
Все команды необходимо выполнять в папке compose
- Остановить все контейнеры
```bash
sudo docker-compose stop
```
- Перезапустить контейнер
```bash
sudo docker-compose restart {container_name}
```
- Запуск manage.py shell
```bash
sudo docker-compose exec backend python manage.py shell
```
