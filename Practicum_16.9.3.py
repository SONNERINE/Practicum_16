# Задача 16.9.3:

# В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо
# создать класс «Клиент», который будет содержать данные о клиентах и их финансовых
# операциях. О клиенте известна следующая информация: имя, фамилия, город, баланс.

# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

# Решение:

class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"Данные клиента: {self.name}, {self.surname}.\n "\
               f"Город: {self.city}\n Баланс: {self.balance} рублей."


client_1 = Clients("Иван", "Петров", "Москва", 50)
print(client_1)