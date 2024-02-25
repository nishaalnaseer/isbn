import logging
from typing import Callable

logger = logging.getLogger(__name__)


class ISBNInvalidLength(Exception):
    def __init__(self, length):
        super().__init__(f"Invalid ISBN, length: {length}, expected length 10 or 13")


class InvalidISBN(ValueError):
    def __init__(self):
        super().__init__(f"Invalid ISBN, value error while parsing")


class ISBN:
    def __init__(self):
        pass

    @staticmethod
    def _multiply10(isbn: str) -> int:
        total = 0
        for index, x in enumerate(isbn):
            multiplier = 1 + index
            total += multiplier * int(x)
        return total

    @staticmethod
    def _multiply13(isbn: str) -> int:
        total = 0
        for index, x in enumerate(isbn):

            if (1 + index) % 2 == 1:
                multiplier = 1
            else:
                multiplier = 3

            total += multiplier * int(x)
        return total

    @staticmethod
    def _check(isbn: str, multiplier: Callable) -> bool:
        mod = 10
        check = int(isbn[-1])
        isbn = isbn[:-1]

        total = multiplier(isbn)

        remainder = total % mod
        calculated = 10 - remainder

        logger.debug(
            f"mod: {mod}, remainder: {remainder}, calculated check: {calculated} "
            f"isbn check: {check} total: {total}"
        )

        remainder_again = calculated % 10

        return remainder_again == check

    @staticmethod
    def check(isbn: str) -> bool:
        isbn = isbn.strip().replace("-", "")
        length = len(isbn)

        try:
            int(isbn)
        except ValueError:
            raise InvalidISBN()

        logging.debug(f"ISBN: {isbn}, length: {length}")

        if length == 10:
            return ISBN._check(isbn, ISBN._multiply10)
        elif length == 13:
            return ISBN._check(isbn, ISBN._multiply13)
        else:
            raise ISBNInvalidLength(length)
