import pytest

def print_depth(data, depth=1):
    for key in data:
        print(f"{key} {depth}")
        if isinstance(data[key], dict):
            print_depth(data[key], depth+1)

class Test1:

    def test1(self, capsys):
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ""
        assert err == ""

    def test2(self, capsys):
        data = {
            "vehicle": {
                "bus": "hundai"
                "car": "buggati"
            }
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "vehicle 1\n"
            "bus 2\n"
            "car 3\n"
        )
        assert err == ""

    def test3(self, capsys):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )
        assert err == ""
