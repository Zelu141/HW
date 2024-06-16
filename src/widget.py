from masks import get_mask_account
from masks import get_mask_card_number
from datetime import datetime


def mask_account_card(cards_number: str) -> str:
    """Функция для маскировки номера карты или счёта"""
    if "Счёт" in cards_number:
        mask_account = f"Счёт {get_mask_account(cards_number[:])}"
    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card


def get_data(data: str) -> str:
    """Функция для возвращения даты в нужный формат"""
    d = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_data("2018-07-11T02:26:18.671407"))
