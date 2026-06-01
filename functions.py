def calculate(a: int | float = 10, b: int | float = 5, operation: str = "sum") -> int | float:
    if operation == "sub":
        return a - b
    return a + b


def format_text(text: str = "Hello World", upper: bool = True) -> str:
    if upper:
        return text.upper()
    return text.lower()


def sum_string_numbers(numbers_string: str = "1,2,3", separator: str = ",") -> int | float:
    string_list = numbers_string.split(separator)
    total_sum = 0
    for item in string_list:
        total_sum += float(item)
    return total_sum