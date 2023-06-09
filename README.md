бот [Нейронытик](https://t.me/kplro_bot)
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
