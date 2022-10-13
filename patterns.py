import re

person_pattern = re.compile(r"([А-ЯЁ][а-яё]+)(\s)([А-ЯЁ][а-яё]+)(\s|)(([А-ЯЁ][а-яё]+)|)")
phone_pattern = re.compile(r"(\+7|8)+(\s*|)(\(|)(\d\d\d)(\)|)(-|\s|)(\d\d\d)(-|)(\d\d)(-|)(\d\d)")
phone_update = r"+7(\4)\7-\9-\11"
added_phone = re.compile(r"(\(|)доб\.\s(\d+)(\)|)")
added_phone_update = r"доб.\2"
