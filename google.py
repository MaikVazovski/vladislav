from googlesearch import search

query = input('Введите запрос:\n')
count = 0
while count != 11:
    for url in search(query):
        print(url)
        count += 1