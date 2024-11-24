print('Hej')

from faker import Faker
fake = Faker('it_IT')

print(fake.name())

print(fake.address())

print(fake.text())