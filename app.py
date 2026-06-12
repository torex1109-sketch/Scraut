import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from pywebio import start_server
from pywebio.input import input, TEXT
from pywebio.output import put_success, put_text


def завантажити_шаблон(ім_я, текст_користувача, довжина_тексту):
    папка = Environment(loader=FileSystemLoader('.'))
    файл_шаблону = папка.get_template('string.html')
    return файл_шаблону.render(name=ім_я, text=текст_користувача, length=довжина_тексту)


def відправити_лист(отримувач, тема, html_код):
    повідомлення = MIMEMultipart()
    повідомлення['From'] = "lutchina@ukr.net"
    повідомлення['To'] = отримувач
    повідомлення['Subject'] = тема
    повідомлення.attach(MIMEText(html_код, 'html'))

    try:
        сервер = smtplib.SMTP_SSL("smtp.ukr.net", 465)
        сервер.login("lutchina@ukr.net", "ZsI0O5IE8J6eUTHN")
        сервер.send_message(повідомлення)
        сервер.quit()
        return True
    except:
        return False


def головна_програма():
    put_text("Сервіс обробки тексту для ДЗ 13")

    ім_я = input("Як вас звати?")
    введений_рядок = input("Введіть будь-який рядок", type=TEXT)
    електронна_пошта = input("Введіть вашу пошту (email)")

    очищений_рядок = введений_рядок.strip()
    довжина_рядка = len(очищений_рядок)

    html_лист = завантажити_шаблон(ім_я, очищений_рядок, довжина_рядка)
    відправити_лист(електронна_пошта, "Результат обчислення ДЗ 13", html_лист)

    put_success(f"Успішно оброблено! Рядок: '{очищений_рядок}' (Довжина: {довжина_рядка}). Лист сформовано!")


if __name__ == '__main__':
    start_server(головна_програма, port=8080)