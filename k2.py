from utils import *

# Тут лежат слова для игры
JSON_LINK = 'https://www.jsonkeeper.com/b/Z32T'


# Главная функция
def main():
    # Получаем имя игрока, создаем экземпляр класса Player
    player = Player(input('Введите имя игрока\n'))
    # Приветствие
    print(f'Привет, {player}!')
    # Создаем экземпляр класса BasicWord
    word = load_random_word(JSON_LINK)
    # Выводим правила игры
    display_rules(word)

    # Цикл с вопросами
    # Пока есть неотвеченные слова
    while word.count_subwords() > player.count_used_subwords():
        # Получаем ввод
        user_word = input().lower().strip()
        # Завершение по желанию игрока
        if user_word == 'stop':
            break
        # Слишком короткое слово
        if len(user_word) < 3:
            print('Слишком короткое слово')
            continue
        # Нет такого слова!
        if not word.is_subword_valid(user_word):
            print('Неверно, попробуйте еще раз')
            continue
        # Уже было!
        if player.is_subword_used(user_word):
            print('Вы уже называли это слово')
            continue
        # Если угадал, добавляем слово в список угаданных слов
        player.add_subword(user_word)
        # Просим ввести следующее слово, если еще остались
        if word.count_subwords() != player.count_used_subwords():
            print(f'Верно, назовите еще {build_phrase(word.count_subwords() - player.count_used_subwords())}')

    # Конец игры, вывод результата
    print(f'Игра завершена, Вы угадали {build_phrase(player.count_used_subwords())} из {word.count_subwords()}')


if __name__ == "__main__":
    main()
