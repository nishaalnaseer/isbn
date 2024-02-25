from copy import deepcopy

from isbn import *
import logging
from random import randint

logging.basicConfig(level=0)


def invalidate_isbns(isbns: list):
    isbns = deepcopy(isbns)
    completed = []

    for isbn in isbns:
        isbn = isbn.strip().replace("-", "")
        place = randint(0, (len(isbn)) - 1)

        random_num = 0
        while True:
            random_num = randint(0, 9)

            if random_num == int(isbn[place]):
                continue
            else:
                break

        isbn = f"{isbn[:place]}{random_num}{isbn[place + 1:]}"
        completed.append(isbn)

    return completed


def test13():
    isbns = [
        "978-1-60309-502-0 ",
        "978-1-60309-517-4 ",
        "978-1-60309-527-3 ",
        "978-1-60309-535-8 ",
        "978-1-60309-520-4 ",
        "978-1-60309-454-2 ",
        "978-1-60309-511-2 ",
        "978-1-60309-492-4 ",
        "978-1-60309-513-6 ",
        "978-1-60309-514-3 ",
        "978-1-60309-508-2 ",
        "978-1-60309-038-4 ",
        "978-1-60309-515-0 ",
        "978-1-60309-505-1 ",
        "978-1-60309-469-6 ",
        "978-1-60309-344-6 ",
        "978-1-60309-526-6 ",
        "978-1-60309-504-4 ",
        "978-1-60309-521-1 ",
        "978-1-891830-02-0 ",
        "978-1-891830-25-9 ",
        "978-1-60309-030-8 ",
        "978-1-60309-412-2 ",
        "978-1-60309-534-1 ",
        "978-1-891830-91-4 ",
        "978-1-60309-067-4 ",
        "978-1-60309-015-5 ",
        "978-1-60309-041-4 ",
        "978-1-60309-084-1 ",
        "9781603093491 ",
        "978-1-60309-384-2 ",
        "978-1-60309-503-7 ",
        "978-1-60309-533-4 ",
        "9781603093682 ",
        "978-1-60309-385-9 ",
        "978-1-60309-500-6 ",
        "978-1-60309-467-2 ",
        "978-1-60309-329-3",
    ]

    for x in isbns:
        assert ISBN.check(x) is True

    wrong = invalidate_isbns(isbns)
    for x in wrong:
        assert ISBN.check(x) is False


def test10():
    pass


if __name__ == '__main__':
    # test13()

    assert ISBN.check("2131110004287") is True
