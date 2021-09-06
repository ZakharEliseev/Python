class Hero():
    """Class to create hero for our game"""

    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parametrs of this hero"""
        stats = (self.name + ' Level is: ' + str(self.level) + ', Race is: ' + self.race + ', Health is: ' + str(
            self.health)).title()
        print(stats)

    def level_up(self):
        """Upgrade level of Hero"""
        self.level += 1

    def move(self):
        """Start moving hero"""
        print('Hero ' + self.name + 'Start moving...')

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """Class to create Super Hero"""

    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100

    def makemagic(self):
        """Use magic"""
        self.__magic -= 10

    def show_hero(self):
        stats = (self.name + ' Level is: ' + str(self.level) + ', Race is: ' + self.race + ', Health is: ' + str(
            self.health) + ", Mmagic is " + str(self.__magic)).title()
        print(stats)