import re

test_text = "{name}, ваша запись изменена: ⌚️ {day_month} в {start_time} 👩 {master} Услуги: {services} управление записью {record_link}"


def check(s: str):
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']
    if s[0] == '{' and s[-1] == '}' and s[1:-1] in list_keys:
        print(f'{s} - корректно')
    else:
        print(f'{s} - ошибка')


def check_correct(arr: str):
    new_arr = ''.join(re.split("[^a-zA-Z{-}_ ]*", arr)).split()
    for i in new_arr:
        check(i)


check_correct(test_text)
