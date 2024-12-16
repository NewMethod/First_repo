import re

def normalize_phone(phone_number):
    # delete all \s symbols
    pattern = r"\s"
    replacement = ""
    phone_number = re.sub(pattern, replacement, phone_number)
    # generate right format numbers
    pattern_number = r"[+\(\)\w\s\\-]*(0\d{2})[\(\)\w\s\\-]*(\d{3})[\(\)\w\s\\-]*(\d{2})[\(\)\w\s\\-]*(\d{2})[\(\)\w\s\\-]*"
    replacement = r"+38\1\2\3\4"
    norm_phones = re.sub(pattern_number, replacement, phone_number)
    return norm_phones

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)