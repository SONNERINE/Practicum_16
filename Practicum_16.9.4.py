# Задача 16.9.4:

# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей. В класс
# «Клиент» добавьте метод, который будет возвращать информацию только об имени,
# фамилии и городе клиента.

# Затем создайте список, в который будут добавлены все клиенты, и выведите его в
# консоль.

# Решение:

class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"Данные клиента: {self.name}, {self.surname}.\n " \
               f"Город: {self.city}\n Баланс: {self.balance} рублей."

    def get_client_guest(self):
        return f"Гость: {self.name} {self.surname}, город: {self.city}"


client_1 = Clients("Ivan", "Smirnov", "Pskov", 120)
client_2 = Clients("Nataly", "Yakimova", "Saratov", 1200)
client_3 = Clients("Ivan", "Petrov", "Moskow", 78)
client_4 = Clients("Elena", "Voynich", "Pskov", 521)


list_guestes = [client_1, client_2, client_3, client_4]

for guest in list_guestes:
    print(guest.get_client_guest())