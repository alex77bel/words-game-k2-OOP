class Player:
    """
    Описывает поведение сущности "Player"
    """

    def __init__(self, name: str) -> None:
        """
        Поля для инициализации состояния экземпляров класса
        """

        self.__name = name
        self.__used_subwords: list = []

    def __repr__(self) -> str:
        """
        Задает отображение экземпляров класса
        """

        return f'{self.__name}'

    def count_used_subwords(self) -> int:
        """
        Получение количества использованных слов
        """

        return len(self.__used_subwords)

    def add_subword(self, word: str) -> None:
        """
        Добавление слова в использованные слова
        """

        self.__used_subwords.append(word)

    def is_subword_used(self, word: str) -> bool:
        """
        Проверка использования данного слова до этого
        """

        return word in self.__used_subwords
