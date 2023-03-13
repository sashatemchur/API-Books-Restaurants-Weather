import requests, json

name_book = str(input("Ведіть ключові слова які є у загаловку твора: "))

book = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={name_book}+intitle:keyes&key=AIzaSyCE1fuJ62Yr3qi_6xKcNt7cmgUh_WxXHA8')

for i in range(10): 
    print(json.loads(book.text)['items'][i]['volumeInfo']['title'], json.loads(book.text)['items'][i]['volumeInfo']['authors'], \
        json.loads(book.text)['items'][i]['volumeInfo']['publishedDate'], json.loads(book.text)['items'][i]['volumeInfo']['infoLink'], '\n\n\n')
