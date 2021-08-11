# parse_website_tengri
# parse data from https://tengrinews.kz/
парсинг данных из указанного веб сайта

Парсер с помощью библиотек requests и BeautifulSoup(bs4) парсит такие данные:

- title статьи
--- text статьи
--- publicated_date дата публикации статьи

------ В качестве Базы данных использовал MySQL.

Если хотите использовать код у себя без Базы данных, можете просто удалить/закомментить
вызов функции для записи в БД.


The parser uses the requests and BeautifulSoup libraries (bs4) to parse the following data:

--- article title
--- text of the article
--- publicated_date publication date of the article

------ Used MySQL as a Database.

If you want to use the code without a Database, you can simply delete / comment out
function call for writing to the database.
