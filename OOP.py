while True:
    class Dog():
        def __init__(self, name_func, lie_func, pet_func):
            self.name = name_func
            self.lie = lie_func
            self.pet = pet_func

        def dog_function(self):
            lie_and_pet = input("Что вы хотите сделать? 'Погладить' собачку или 'Полаять': ")
            if lie_and_pet == str('Погладить'):
                return 'Вы погладили ' + self.name + 'а!'
            elif lie_and_pet == str('Полаять'):
                return 'Ваша собачка ' + self.name + ' полаяла!'
            else:
                return 'Неизвестное действие. Пожалуйста, введите "Погладить" или "Полаять".'


    my_dog = Dog(input(str("Как будут звать вашего пса?: ")), 'Лаять', 'Погладить')
    result = my_dog.dog_function()
    print(result)
    break