
## Установка и запуск 
1. Клонировать проект
```
git clone https://github.com/ivangol739/data_shop
```     
2. Перейти в каталог проекта
```
cd data_shop
```  
3. Создать и активировать виртуальное окружение

**Windows**
```
python -m venv venv
venv\Scripts\activate
```  
**macOS и Linux**
```
python3 -m venv venv
source venv/bin/activate
```
4. Установить зависимости
```
pip install -r requirements.txt
```  
5. Настройка переменных окружения. Создать файл `.env` в корневом каталоге и добавить DSN.
```
DSN = 'postgresql+psycopg2://{login}:{password}@localhost:5432/db_shop_book'
```  
6. Создать БД
```  
createdb -U postgres db_shop_book
```  
7. Запустить проект
```
python main.ru
```  