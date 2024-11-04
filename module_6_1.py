class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name   # Имя животного

# Базовый класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name     # Имя растения

# Класс Mammal, наследующий от Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Predator, наследующий от Animal
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Flower, наследующий от Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

# Класс Fruit, наследующий от Plant и переопределяющий edible
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем на съедобное

# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка состояния объектов и выполнение действий
print(a1.name)  # Вывод имени хищника
print(p1.name)  # Вывод имени цветка

print(a1.alive)  # Проверка состояния жизни хищника
print(a2.fed)    # Проверка состояния накормленности млекопитающего

# Попытка покормить животных растениями
a1.eat(p1)  # Хищник пытается съесть цветок (несъедобное)
a2.eat(p2)  # Млекопитающее пытается съесть фрукт (съедобное)

print(a1.alive)  # Проверка состояния жизни хищника после еды
print(a2.fed)    # Проверка состояния накормленности млекопитающего после еды