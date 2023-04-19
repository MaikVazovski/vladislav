from googlesearch import search

query = input('Введите запрос:\n')
count = 0
for url in search(query):
    for i in range(10):
        print(url)