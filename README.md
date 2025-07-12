<h2>Автотесты на API проекта «Битва покемонов»</h2>

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизировали
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests

![image](https://raw.githubusercontent.com/Elena-Grinyak-QA/Python_autotests/refs/heads/main/2025-07-12_14-55-06.png)


## Автор

Елена Гриняк ([@elena_grinyak](https://t.me/elena_grinyak))
