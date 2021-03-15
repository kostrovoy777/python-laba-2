import random

from faker import Faker

job = ('дизайнер', 'программист', 'тестировщик', 'аналитик')
division = ('маркетинг', 'бэкэнд', 'фронтэнд', 'администрирование')
random.seed(version=2)
FILENAME = "members.csv"

if __name__ == '__main__':
    f = open(FILENAME, 'w')
    fake = Faker('ru_RU')
    for i in range(1, 101):
        f.write(str(i) + " " + fake.name() + "; " + fake.random_element(elements=job) + "; " + fake.random_element(
            elements=division) + "; " + str(random.randint(1, 5)) + "; " + str(random.randint(800, 1200)) + "00; \n")
    f.close()
