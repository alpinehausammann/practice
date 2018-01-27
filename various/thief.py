import random

class Character:

    def __init__(self, name, **kwargs)
        self.name = name

        for key, value in kwargs.items():
            # setattr allows us to name attributes that
            # havent been created.
            setattr(self, key, value)
class Thief:
    sneaky = True

    def __init__(self, name, **kwargs):
        


    def pickpocket(self, sneaky):
