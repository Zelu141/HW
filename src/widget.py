from datetime import datetime


def get_mask_account(account: str) -> str | None:
    """Фукнция маскирующая номер счёта"""
    if account.isdigit() and len(account) == 20:
        return f"**{account[-4::]}"
    else:
        return None


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер счёта"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return None
