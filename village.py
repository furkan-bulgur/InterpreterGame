
# Resource keywords
FOOD = "FOOD"

#Default values
DEFAULT_INITIAL_FOOD = 10

class Town:

    def __init__(self, name="unnamed", initial_food=DEFAULT_INITIAL_FOOD):
        self._resources = {}
        self._name = name
        self._resources[FOOD] = initial_food

    @property
    def name(self):
        return self._name

    @property
    def food(self):
        return self._resources[FOOD]

    def info(self):
        str = """
        {name} Town
            Food: {food}
        """.format(name=self.name,food=self.food)

        return str


if __name__ == '__main__':
    print(Town("Hulalu").info())