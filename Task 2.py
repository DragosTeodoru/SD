class Animal:
    def __init__(self):
        self.name = "init"
        self.age = 0
        self.prefered_environment = ""

    def set_name(self, value):
        self.name = value

    def set_age(self, value):
        self.age = value

    def set_environment(self, value):
        self.prefered_environment = value


class Insect(Animal):
    def __init__(self):
        super().__init__()
        self.insect_type = ""
        self.insect_color = ""
        self.insect_food_preference = ""

    def set_insect_type(self, value):
        self.insect_type = value

    def set_insect_color(self, value):
        self.insect_color = value

    def set_insect_food(self, value):
        self.insect_food_preference = value


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.mammal_fur_color = ""
        self.mammal_food_preference = ""
        self.mammal_lactation_type = ""

    def set_mammal_fur_color(self, value):
        self.mammal_fur_color = value

    def set_mammal_food_preference(self, value):
        self.mammal_food_preference = value

    def set_mammal_lactation_type(self, value):
        self.mammal_lactation_type = value


class Bee(Insect):
    def __init__(self, name, age):
        super().__init__()
        super().set_name(name)
        super().set_age(age)
        super().set_environment("Air")


class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__()
        super().set_name(name)
        super().set_age(age)
        super().set_environment("Ground")


class TestDog:
    def test_beagle(self):
        beagle = Dog("Beagle", "2 years")
        beagle.set_mammal_fur_color("Brown and White")
        beagle.set_mammal_lactation_type("Breast lactation")
        beagle.set_mammal_food_preference("Carnivore")

        print(
            "NAME : {0} / AGE : {1} / Prefered Environment : {2} / Fur Color: {3} / Food Preference : {4} / Lactation Type : "
            "{5}".format(beagle.name, str(beagle.age), beagle.prefered_environment, beagle.mammal_fur_color,
                         beagle.mammal_food_preference, beagle.mammal_lactation_type))


class TestBee:
    def test_bee(self):
        bondar = Bee("Bumble-bee", "4 days")
        bondar.set_insect_color("Yellow and Black")
        bondar.set_insect_food("Pollen")
        bondar.set_insect_type("Flying Insect")

        print(
            "NAME : {0} / AGE : {1} / Prefered Environment : {2} / Insect Color: {3} / Food Preference : {4} / Insect Type : {5}".format
            (bondar.name, str(bondar.age), bondar.prefered_environment, bondar.insect_color,
             bondar.insect_food_preference, bondar.insect_type))


TestDog().test_beagle()
TestBee().test_bee()
