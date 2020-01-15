from helloworld import get_greetings
from helloworld import fizzbuzz


def test_get_helloworld():
    assert get_greetings() == 'Hello World!'
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(15) == 'fizzbuzz'
