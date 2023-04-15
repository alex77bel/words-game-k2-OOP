class BasicWord:
    """
    Описывает поведение сущности "BasicWord"
    """

    def __init__(self, data: dict) -> None:
        """
        Поля для инициализации состояния экземпляров класса
        """

        self.__word = data['word']
        self.__subwords = data['subwords']

    def __repr__(self) -> str:
        """
        Задает отображение экземпляров класса
        """

        return f'{self.__word}'

    def is_subword_valid(self, word: str) -> bool:
        """
        Проверка введенного слова в списке допустимых подслов
        """

        return word in self.__subwords

    def count_subwords(self) -> int:
        """
        Подсчет количества подслов в слове
        """

        return len(self.__subwords)
