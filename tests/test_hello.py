from src import hello_world


def test_hello_world():
    assert hello_world.hello() == "Hello World!"
