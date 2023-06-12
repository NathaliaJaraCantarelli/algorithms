from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('nathalia', 2) == 'ailaht_an'
    assert encrypt_message('nathalia', 3) == 'tan_ailah'
    assert encrypt_message('nathalia', 9) == 'ailahtan'

    with pytest.raises(TypeError):
        encrypt_message(55, 5)

    with pytest.raises(TypeError):
        encrypt_message('nathalia', 'nathalia')
