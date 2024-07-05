from typing import Any


def get_filtered_and_sorted(data):
    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)
    return items

def prepare_user_msg(item: dict[str, Any]):
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = mask_from_to(item.get('from'))
    to_ = mask_from_to(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    currency = item.get('operationAmount').get('currency').get('name')

    if from_:
        from_ += ' ->'

    else:
        from_ = ''

    return f"{date} {desc}\n{from_}{to_}\n{amount} {currency}"

def get_date(date):
    date_raw = date[0:10].split(sep="-")
    return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"


def mask_from_to(number):
    if number is None:
        return ""

    msg = number.split()

    if msg[0] == "Счет":
        number_hidden = mask_account(msg[-1])
    else:
        number_hidden = mask_card_number(msg[-1])

    return ' '.join(msg[:-1]) + ' ' + number_hidden


def mask_account(number):
    if number.isdigit() and len(number) > 4:
        return f"**{number[-4:]}"

    else:
        raise ValueError("Номер счета не валидный")


def mask_card_number(number: str):
    if number.isdigit() and len(number) > 4:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    else:
        raise ValueError("Номер карты не валидный")