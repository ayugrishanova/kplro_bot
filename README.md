Ссылка на бота: [Нейронытик](https://t.me/kplro_bot)
# О создании бота
Использована предуобученная сеть генерации текста на русском языке от [Сбербанка](https://huggingface.co/sberbank-ai/rugpt3large_based_on_gpt2). Fine-tuning производился на небольшом корпусе текстов с сайта https://killpls.me -- там люди делятся своими проблемами, используя своеобразную лексику и синтаксические конструкции. Процесс fine-tuning'а можно проследить в тетрадке **прога_проект.ipynb**.
Модель была загружена мной на сервис [hugging-face](https://huggingface.co/kplro/model_proga), к модели обращаюсь через api.

В репозитории лежит четыре файла с разрешением .py.
Файл | Его предназначение
---- | ----
bot.py | В нем написан сам код бота
cloud.py | В нем лежит функция для создания облака слов
conf.py | Файл с персональными ключами для hugging-face и для pythonanywhere
my_model.py | В нем мы обращаемся к сервису api hugging-face, где лежит моя обученная модель

Бот запущен с помощью pythonanywhere в [консоли pythonanywhere](https://www.pythonanywhere.com/user/kplro/files/home/kplro/telegram_bot/bot.py), поэтому нет необходимости запускать его локально. Так как в боте не используются базы данных, я посчитала, что оборачивать его в flasker бессмысленно -- он и так работает.

Итак, в проекте используются:
- предобученная нейросеть и fine-tuning
- морфологический парсинг для создания облака слов
- картинки в боте для отправки облака слов
- различные кнопки для навигации по боту + встроенная клавиатура для особых ответов
- слежка за историей диалога, возможность очистить историю
# Функционал бота
Бот продолжает фразы пользователя, имитируя людей, делящихся своими проблемами. Таким образом, пользователь отправляет сообщение с текстом на русском языке, а бот взамен через пару минут присылает небольшую историю, рассказанную эмоционально. В любой момент пользователь может "успокоить бота" -- завершить сеанс. В конце каждого сеанса пользователю предлагают создать облако слов по мотивам беседы. В начале сеанса пользователя спрашивают, "Смешарик ли он", то есть, хочет ли он продолжить уже начатую беседу. Даже если человек уже пользовался ботом, при нажатии кнопки "Я новенький" история стирается.

---

Bot link: [Neurowhiner](https://t.me/kplro_bot)
# About the creation
I use a pre-trained Russian text generation model [Sberbank](https://huggingface.co/sberbanka i/rugpt3large_based_on_gpt2). Fine-tuning was performed on a small corpus of texts from the website https://killpls.me, where people share their problems using peculiar vocabulary and syntactic constructions. The process of fine-tuning can be traced in the notebook **proga_project.ipynb**.
The model was uploaded by me to the [huggingface] service(https://huggingface.co/pro/model_proga ), I access the model via the api.

The repository contains four .py files.

File | Its contents
---- | ----
bot.py | The code of the bot application
cloud.py | Word cloud function
conf.py | File with token keys to hugging-face and pythonanywhere
my_model.py | Use of huggingface api with the fine-tuned model

The bot is launched using pythonanywhere in [pythonanywhere console](https://www.pythonanywhere.com/user/kplro/files/home/kplro/telegram_bot/bot.py ), so there is no need to run it locally. Since the bot does not use databases, I thought it would be pointless to wrap it in flasker - it already works.

So, the project uses:
- a pre-trained neural network and fine-tuning
- morphological parsing to create a word cloud
- images in the bot to send a word cloud
- various buttons for navigating the bot + built-in keyboard for special responses
- tracking the history of the dialogue, the ability to clear the history

# Bot functionality
The bot continues the user's phrases, imitating people sharing their problems. Thus, the user sends a message with a text in Russian, and in return, after a couple of minutes, the bot sends a short story told emotionally. At any time, the user can "calm the bot down" -- end the session. At the end of each session, the user is offered to create a word cloud based on the conversation. At the beginning of the session, the user is asked if he is "Smesharik", that is, if he wants to continue the conversation he has already started. Even if the person has already used the bot, when the "I'm new" button is clicked, the history is erased.
