"""Main is a package to create the game's characters."""

from __future__ import annotations

from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str | None:
    """Generate attack points.
    
    The attack points depend on a game character that is selected a player.

    Args:
    char_name: The name of a player.
    char_class: The type of a game character.

    Returns:
    The message about the attack or `None`.
    """
    damage: int = None

    if char_class == 'warrior':
        damage = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {damage}')

    if char_class == 'mage':
        damage = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {damage}')

    if char_class == 'healer':
        damage = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {damage}')

    return None


def defence(char_name: str, char_class: str) -> str | None:
    """Generate protection points.
    
    The protection points depend on a game character that is selected a player.

    Args:
    char_name: The name of a player.
    char_class: The type of a game character.

    Returns:
    The message about the blocked attack or `None`.
    """
    blocked: int = None

    if char_class == 'warrior':
        blocked = 10 + randint(5, 10)
        return (f'{char_name} блокировал {blocked} урона')

    if char_class == 'mage':
        blocked = 10 + randint(-2, 2)
        return (f'{char_name} блокировал {blocked} урона')

    if char_class == 'healer':
        blocked = 10 + randint(2, 5)
        return (f'{char_name} блокировал {blocked} урона')

    return None


def special(char_name: str, char_class: str) -> str:
    specifical_skill: int = None

    if char_class == 'warrior':
        specifical_skill = 80 + 25
        return (f'{char_name} применил специальное умение «Выносливость'
                f'{specifical_skill}»')

    if char_class == 'mage':
        specifical_skill = 5 + 40
        return (f'{char_name} применил специальное умение «Атака'
                f'{specifical_skill}»')

    if char_class == 'healer':
        specifical_skill = 10 + 30
        return (f'{char_name} применил специальное умение «Защита'
                f'{specifical_skill}»')

    return None


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence',
          ' — чтобы блокировать атаку противника или special',
          ' — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))

    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь '
                           'играть: Воитель — warrior, Маг — mage, Лекарь '
                           '— healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый',
                  ' и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким',
                  ' интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из',
                  ' природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую'
                               ' другую кнопку, чтобы выбрать другого'
                               ' персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
