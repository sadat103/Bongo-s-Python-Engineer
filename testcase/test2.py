import pytest


class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def print_depth(data, depth=1):

    if isinstance(data, Person):
        names = ["first_name", "last_name", "father"]
        for n in names:
            print(f"{getattr(data, n)} {depth}")
        if isinstance(data.father, Person):
            print_depth(data.father, depth + 1)

    elif isinstance(data, dict):
        for key in data:
            print(f"{key} {depth}")
            if isinstance(data[key], object):
                print_depth(data[key], depth + 1)


class Test2:

    @pytest.fixture
    def person_a(self):
        return Person("Hedge", "Gimme", None)

    @pytest.fixture
    def person_b(self, person_a):
        return Person("Hossain", "Hunter", person_a)

    def test_empty(self, capsys):
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ""
        assert err == ""

    def test2(self, capsys, person_b):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            },
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "Walter 4\n"
            "Melon 4\n"
            "Paige Turner 4\n"
            "Paige 5\n"
            "Turner 5\n"
            "None 5\n"
        )
        assert err == ""
