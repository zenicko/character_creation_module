"""Main is a package to create the game's characters."""

from __future__ import annotations

from random import randint

from graphic_arts.start_game_banner import run_screensaver


class Character:
    DEFAULT_ATTACK = 5
    RANGE_VALUE_ATTACK = (0, 0)
    DEFAULT_DEFENCE = 10
    RANGE_VALUE_DEFENCE = (0, 0)
    SPECIAL_SKILL = ''
    SPECIAL_BUFF = 0
    BRIEF_DESC_CHAR_CLASS = ''
    DEFAULT_STAMINA = 80

    def __init__(self, name: str):
        self.name = name

    def attack(self):
        value_attack = (Character.DEFAULT_ATTACK +
                        randint(*self.__class__.RANGE_VALUE_ATTACK))
        return f'{self.name} нанёс противнику урон, равный {value_attack}'

    def defence(self):
        value_defence = (Character.DEFAULT_DEFENCE +
                         randint(*self.__class__.RANGE_VALUE_DEFENCE))
        return f'{self.name} блокировал {value_defence} ед. урона'

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'«{self.__class__.SPECIAL_SKILL} '
                f'{self.__class__.SPECIAL_BUFF}».')

    def __str__(self) -> str:
        return f'{self.name} - {self.__class__.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = ('Воитель — дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный.')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = Character.DEFAULT_STAMINA + 25


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = ('Маг — находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом.')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = Character.DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = ('Лекарь — могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов.')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = Character.DEFAULT_DEFENCE + 30


def start_training(character: Character) -> str:
    """Start the training of a skill of a game character.

    Args:
    char_name: The name of a player.
    char_class: The type of a game character.

    Returns:
    The message `The training is over.`(en) or `Тренировка окончена.`(ru).
    """
    print()
    if type(character) == Warrior:
        print(f'{character.name}, ты Воитель — отличный боец ближнего боя.')
    if type(character) == Mage:
        print(f'{character.name}, ты Маг — превосходный укротитель стихий.')
    if type(character) == Healer:
        print(f'{character.name}, ты Лекарь — чародей, способный исцелять'
              f'раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence',
          ' — чтобы блокировать атаку противника или special',
          ' — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    commands = {'attack': character.attack,
                'defence': character.defence,
                'special': character.special
                }
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd]())

    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Choice the type of a game character.

    Returns:
    The type of a game character.
    """
    approve_choice: str = None
    game_classes: dict = {
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer
    }
    character: Character = None
    while approve_choice != 'y':
        select_class = input('Введи название персонажа, за которого хочешь '
                             'играть: Воитель — warrior, Маг — mage, Лекарь '
                             '— healer: ')
        character = game_classes[select_class](char_name)
        print(character)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую'
                               ' другую кнопку, чтобы выбрать другого'
                               ' персонажа ').lower()
    return character


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character: Character = choice_char_class(char_name)
    print(start_training(character))
