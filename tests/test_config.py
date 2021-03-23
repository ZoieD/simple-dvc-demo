
import pytest

class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.messsage = message
        super().__init__(self.messsage)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange

def test_somthing():
    a = 2
    b = 2
    assert True
