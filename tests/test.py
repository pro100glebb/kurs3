from utils import get_date, mask_from_to

def test_get_date():
    assert get_date("2018-08-14T05:42:30.104666") == "14.08.2018"


def test_mask_from_to():
    assert mask_from_to("Счет 98841213648056852372") == "Счет **2372"