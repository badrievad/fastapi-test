import re


def camel_to_snake(name: str) -> str:
    """
    Преобразует строку из CamelCase в snake_case.
    Например, 'OrderProductAssociation' -> 'order_product_association'.
    """
    # Вставляем подчеркивание между строчными и заглавными буквами
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Вставляем подчеркивание между цифрой/строчной и заглавной буквой
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()
