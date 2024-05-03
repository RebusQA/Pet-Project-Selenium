
import pytest

@pytest.fixture()
def set_up():
    print("\nStart test\n")
    yield
    print("\nFinish test")