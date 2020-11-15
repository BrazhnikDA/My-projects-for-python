# Бот для отправки расписания в ВК

**!В коде указан токен группы, я знаю что так делать нельзя,но мне эта группа не нужна!**

Принцип работы:
	1. Отправляем пользователю клавиатуру
	2. Слушаем нажатие кнопки
	3. По нажатой кнопке выбираем наше последующее действие
	
В файле statistics хранятся данные по количеству запросов от всех польхователей использующих бота, в документе содержится 5 строк
	1. Нажатие на кнопку Сегодня
	2. Нажатие на кнопку Завтра
	3. Нажатие на кнопку Вся неделя
	4. Нажатие на кнопку Расписание звонков
	5. Бот не смог понять что ответить

5 пункт не вижу смысла как-то обрабатывать, это единичные случаи когда человек решил что-то ввести с клавиатуры

## Библиотеки которые я использовал
```
	import json							
	from datetime import datetime

	# VK_API
	from vk_api import VkApi
	from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
	from vk_api.upload import VkUpload
	from vk_api.utils import get_random_id
```