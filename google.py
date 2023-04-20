from googlesearch import search

query = input('Введите запрос:\n')
count = 0
for url in search(query):
    print(url)