from faker import Faker

fake = Faker('ru_RU')
# print(fake.zip())
print(dir(fake))


print(f'Фейковое имя: {fake.name()}')
print(fake.address())
print(fake.phone_number())
print(fake.city())
print(fake.bank())
print(fake.password(length=10))
print(fake.job())
print(fake.firefox())
print(fake.email())
print(fake.time())
print(fake.credit_card_full())