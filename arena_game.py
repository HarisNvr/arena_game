from random import choice, randint, uniform, sample
from colorama import init, Fore
from decimal import Decimal

init(autoreset=True)

NAMES = [
    "Azura", "Caspian", "Elysia", "Finnian", "Isolde", "Lysander",
    "Maeve", "Orion", "Persephone", "Soren", "Thalia", "Vesper",
    "Xanthe", "Zephyr", "Aurelia", "Cyrus", "Dahlia", "Ezra",
    "Nova", "Ragnar"
]

SURNAMES = [
    "Blackwood", "Stark", "Silverstone", "Stormborn", "Frost", "Moonshadow",
    "Winters", "Firestone", "Nightshade", "Ravenwood", "Whitewood", "Dawnsong",
    "Everhart", "Wolfbane", "Starfall", "Ironheart", "Stoneforge", "Trueblood",
    "Skywalker", "Dragonfyre"
]


class Thing:
    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp


ALL_THINGS = [
    Thing("Armor", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Chain mail", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Sword", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Helmet", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Boots", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Belt", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Ring", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Staff", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
    Thing("Amulet", round(uniform(0.01, 0.1), 2),
          randint(1, 10), randint(1, 10)),
]


class Person:
    def __init__(self):
        self.chr_name = None
        self.chr_hp = Decimal(100)  # Базовое здоровье персонажа - 100 у.е
        self.chr_armor = Decimal(0.1)  # Базовая броня персонажа - 10%
        self.chr_attack = Decimal(10)  # Базовая атака персонажа - 10 у.е
        self.equipped_things = []  # Начальный пустой список "надетых" вещей

    def set_things(self, things):
        for thing in things:
            self.equipped_things.append(thing)
            self.chr_armor = self.chr_armor + Decimal(thing.protection)
            self.chr_attack = self.chr_attack + Decimal(thing.attack)
            self.chr_hp = self.chr_hp + Decimal(thing.hp)

    def subtract_hp(self, attack):
        self.damage_taken = ((attack - attack * self.chr_armor).
                             quantize(Decimal("1.00")))
        self.chr_hp -= self.damage_taken


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.chr_hp *= 2
        self.chr_armor *= 2


class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.chr_attack *= 2


def main():
    # Логика игры
    players_count = 4
    players = []
    i = 0
    fight_num = 1
    used_names = set()

    while i < players_count:
        player = choice((Paladin(), Warrior()))
        name = f'{choice(NAMES)} {choice(SURNAMES)}'

        while name in used_names:
            name = f'{choice(NAMES)} {choice(SURNAMES)}'

        player.chr_name = name
        used_names.add(name)

        players.append(player)
        i += 1

    for player in players:
        player.set_things(sample(ALL_THINGS, randint(0, 4)))

    running = True

    while running:
        fighters = sample(players, k=2)
        attacking, defending = fighters

        print(Fore.BLUE + f'\n'
                          f'Начинается {fight_num}-й бой '
                          f'между {attacking.chr_name} ({attacking.chr_hp} HP) '
                          f'и {defending.chr_name} ({defending.chr_hp} HP)!'
                          f'\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        while attacking.chr_hp > 0 or defending.chr_hp > 0:
            dnd_dice = randint(1, 20)
            if dnd_dice == 1:
                attacking.subtract_hp(attacking.chr_attack)
                print(Fore.LIGHTMAGENTA_EX + f'{attacking.chr_name} '
                                             f'критически промахивается '
                                             f'по {defending.chr_name} '
                                             f'и наносит сам себе '
                                             f'{attacking.damage_taken} урона')
            elif 2 <= dnd_dice <= 5:
                print(Fore.LIGHTGREEN_EX + f'{attacking.chr_name} '
                                           f'промахивается по '
                                           f'{defending.chr_name}')
            elif 6 <= dnd_dice <= 9:
                defending.subtract_hp(attacking.chr_attack * Decimal(0.5))
                print(Fore.LIGHTYELLOW_EX + f'{attacking.chr_name} '
                                            f'наносит слабый '
                                            f'удар по {defending.chr_name} на '
                                            f'{defending.damage_taken} урона')
            elif 10 <= dnd_dice <= 19:
                defending.subtract_hp(attacking.chr_attack)
                print(Fore.LIGHTWHITE_EX + f'{attacking.chr_name} '
                                           f'наносит удар по '
                                           f'{defending.chr_name} на '
                                           f'{defending.damage_taken} урона')
            elif dnd_dice == 20:
                defending.subtract_hp(attacking.chr_attack * Decimal(2))
                print(Fore.LIGHTRED_EX + f'{attacking.chr_name} '
                                         f'наносит КРИТИЧЕСКИЙ '
                                         f'удар по {defending.chr_name} на '
                                         f'{defending.damage_taken} урона')

            print(
                f'----------HP----------'
                f'\n{attacking.chr_name} - '
                f'{attacking.chr_hp if attacking.chr_hp > 0 else int(0)}')
            print(
                f'{defending.chr_name} - '
                f'{defending.chr_hp if defending.chr_hp > 0 else int(0)}')

            if attacking.chr_hp <= 0 or defending.chr_hp <= 0:
                print(Fore.BLUE + '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
                players.remove(defending)
                break

            print('\n')

            attacking, defending = defending, attacking
        fight_num += 1

        if len(players) == 1:
            running = False
            print(Fore.CYAN + f'\n'
                              f'Игра окончена, победил '
                              f'{players[0].__class__.__name__} '
                              f'{players[0].chr_name}')


if __name__ == '__main__':
    main()
