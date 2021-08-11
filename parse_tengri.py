"""app for parse data from website"""
import requests
from bs4 import BeautifulSoup as BS
import mysql.connector


def get_date_from_tengri(requests, BS, html, mysql_connector):
    """func for parse date(title, text, pub_date)
    with bs4, requests from https://tengrinews.kz"""
    try:
        for line in html.find_all('a', 'tn-tape-title', href=True):
            date_tuple = ()
            r = requests.get('https://tengrinews.kz' + line['href'])
            soup = BS(r.content, 'html.parser')
            # .next_element.strip() удаляет лищние данные из span
            # которая так же находится внутри h1
            title = soup.find('h1', 'tn-content-title').next_element.strip()
            date_tuple += (title,)
            # print(date_tuple)
            text = soup.find('article', 'tn-news-text')
            date_tuple += (text.text,)
            pub_time = soup.find('li', 'tn-hidden@t')
            date_tuple += (pub_time.text,)
            add_data_to_db(mysql_connector, date_tuple)
    except AttributeError:
        print('Перебор закончен')
    finally:
        print('Процесс закончен')


def add_data_to_db(mysql_connector, data):
    mydb = mysql_connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="date_website",
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO tengri_data (title, text, date) VALUES (%s, %s, %s)"
    mycursor.execute(sql, data)

    mydb.commit()

    print(f"Добавлено {mycursor.rowcount} поле")


if __name__ == "__main__":
    r = requests.get('https://tengrinews.kz/')
    html = BS(r.content, 'html.parser')
    get_date_from_tengri(requests, BS, html, mysql.connector)

    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="",
    #     database="date_website",
    # )
    #
    # mycursor = mydb.cursor()
    #
    # sql = "SELECT * FROM tengri_data"
    # mycursor.execute(sql)
    #
    # myresult = mycursor.fetchall()
    #
    # for x in myresult:
    #     print(x)




