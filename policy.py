import random

class Policy:
    def __init__(self, name, description, effect_functions):
        self.name = name
        self.description = description
        self.effect_functions = effect_functions  # dict of { 'variable': function }

    def apply(self):
        effects = {}
        for variable, func in self.effect_functions.items():
            effects[variable] = func()
        return effects

def create_default_policies():
    return [
        Policy(
            "Raise Taxes",
            "Increase government revenue.",
            {
                "dinero": lambda: random.randint(10, 30),
                "felicidad": lambda: random.choice([-10, -5, 0])
            }
        ),
        Policy(
            "Invest in Health",
            "Improve health services at a fiscal cost.",
            {
                "dinero": lambda: -random.randint(15, 25),
                "salud": lambda: random.randint(5, 15),
                "felicidad": lambda: random.choice([0, 3, 5])
            }
        )
    ]
