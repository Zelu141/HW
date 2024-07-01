def get_mask_card_number(card_number: str) -> str | None:
    # Проверка, что номер карты содержит только цифры и имеет допустимую длину
    if card_number.isdigit() and len(card_number) == 16:
        return card_number[:4] + " 79** **** " + card_number[-4:]
    else:
        return None


def get_mask_account(account: str) -> str | None:
    """Фукнция маскирующая номер счёта"""
    if account.isdigit() and len(account) == 20:
        return f"**{account[-4::]}"
    else:
        return None


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
