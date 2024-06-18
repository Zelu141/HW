from src.masks import get_mask_account
from src.masks import get_mask_card_number
from datetime import datetime


def mask_account_card(payment_info: str) -> str | None:
    """Функция для маскировки номера карты или счёта"""
    payment_data = payment_info.split(" ")
    number = payment_data.pop(-1)
    if "Счет" in payment_info:
        mask_payment_number = get_mask_account(number)
    else:
        mask_payment_number = get_mask_card_number(number)
    if mask_payment_number:
        payment_data.append(mask_payment_number)
        return " ".join(payment_data)
    raise ValueError("Не верный формат данных")


def get_data(data: str) -> str:
    """Функция для возвращения даты в нужный формат"""
    d = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_data("2018-07-11T02:26:18.671407"))
