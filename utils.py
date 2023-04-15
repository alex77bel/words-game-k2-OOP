from random import choice
from requests import get
from player import Player
from basic_word import BasicWord


def load_random_word(link: str) -> BasicWord:
    """
    Загружает JSON, выбирает из него случайное слово,
    создает экземпляр класса BasicWord и возвращает его
    """

    response = get(link)
    return BasicWord(choice(response.json()))


def build_phrase(n: int) -> str:
    """
    Возвращает фразу '... слов' в правильном падеже
    """

    return str(n) + (' слов' if n % 10 in (0, *range(5, 10)) or n % 100 in range(10, 21)
                     else ' слова' if n % 10 in range(2, 5) else ' слово')


def display_rules(word: BasicWord) -> None:
    """
    Выводит правила игры
    """

    print(f'Составьте {build_phrase(word.count_subwords())} из слова "{word}".'
          f'\nСлова должны быть не короче 3 букв.'
          f'\nЧтобы закончить игру, угадайте все слова или напишите "stop".'
          f'\nИтак, какое первое слово?')
