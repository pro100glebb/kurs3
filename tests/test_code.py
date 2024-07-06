from utils import get_date, mask_from_to, mask_account, mask_card_number, get_filtered_and_sorted
import pytest
import json

def test_get_date():
    assert get_date("2018-08-14T05:42:30.104666") == "14.08.2018"
    assert get_date("2018-08-14") == "14.08.2018"
    assert get_date("abc") == ""
    assert get_date("") == ""


def test_mask_from_to():
    assert mask_from_to("Счет 98841213648056852372") == "Счет **2372"
    assert mask_from_to(None) == ""
    assert mask_from_to("Счет 988412136") == "Счет **2136"
    assert mask_from_to("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_mask_account():
    assert mask_account("1596837868705199") == "**5199"
    assert mask_account("159683786452458705199") == "**5199"
    assert mask_account("159683786") == "**3786"
    with pytest.raises(ValueError, match="Номер счета не валидный"):
        mask_account("199")
    with pytest.raises(ValueError, match="Номер счета не валидный"):
        mask_account("oefhwofhefh")

def test_mask_card_number():
    assert mask_card_number("1596837868705199") == "1596 83** **** 5199"
    with pytest.raises(ValueError, match="Номер карты не валидный"):
        mask_card_number("199")
    with pytest.raises(ValueError, match="Номер карты не валидный"):
        mask_card_number("oefhwofhefh")
    with pytest.raises(ValueError, match="Номер карты не валидный"):
        mask_card_number("159683786452458705199")

def test_get_filtered_and_sorted_stated():
    items = '''[{
    "id": 441945886,
    "state": "test",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
    "id": 41428829,
    "state": "test",
    "date": "2019-07-03T18:35:29.512364"
  }
    ]'''
    json_objects = json.loads(items)
    assert get_filtered_and_sorted(json_objects) == []

def test_get_filtered_and_sorted_date():
    items = '''[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
  }
    ]'''
    json_objects = json.loads(items)
    result = get_filtered_and_sorted(json_objects)
    assert result[0]['date'] > result[1]['date']




