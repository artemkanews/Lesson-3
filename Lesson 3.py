import os
import smtplib
from dotenv import load_dotenv


load_dotenv()

login = os.getenv('login')
password = os.getenv('password')


mail_from = "agaevartemka@yandex.ru"
mail_to = "agaevartemka@yandex.ru"
website = 'https://dvmn.org/profession-ref-program/artemkanews/onAPD/'
friend_name = "Эльдар"
my_name = 'Артём'
subject = 'Урок'

letter = """\
From: {3}
To: {4}
Subject: {5}
Content-Type: text/plain; charset="UTF-8";

Привет, {1}! {2} приглашает тебя на сайт {0}!

{0} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {0}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {0}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
""".format(website, friend_name, my_name, mail_from, mail_to, subject)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login (login, password)
server.sendmail(mail_from, mail_to, letter)
server.quit()

