class WrongKeyError(Exception):
    """Отсутствует нужный ключ."""

    pass


class UnknownWorkStatusException(Exception):
    """Передан неизвестный статус работы."""

    pass


class BotMalfunctionError(Exception):
    """Сбой в работе Бота."""

    pass
