#------------------------------------------------------------------------------
# Розробити скрипт для аналізу файлів логів, який повинен виводити статистику
#   лог-файла, переданого як аргумент, за рівнями логування INFO, ERROR, DEBUG
# Користувач може вказати рівень логування як другий аргумент, щоб отримати
#   всі записи цього рівня.
#------------------------------------------------------------------------------
# parse
def parse_log_line(line: str) -> dict:
    data, time, level, message = line.split(' ', 3)
    dict_from_line = dict(data=data, time=time, level=level, message=message)
    return dict_from_line
# load
def load_logs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as fh:
            lines = [parse_log_line(el.strip()) for el in fh.readlines()]
        return lines
    except FileNotFoundError:
        print('The file with such name or path doesn\'t exist')
list_of_logs = load_logs('log_file.bin')
# filter
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda line: line['level'] == level, logs))
# count
def count_logs_by_level(logs: list) -> dict:
    from collections import defaultdict
    level_counter = defaultdict(int)
    for log in logs:
        level_counter[log['level']] += 1
    return dict(level_counter)
counted_by_level = count_logs_by_level(list_of_logs)
# print
def display_log_counts(counts: dict, *args):
    print(' Рівень логування |   Кількість')
    print('-'.join(['' for el in range(0, 35)]))
    for key, value in counts.items():
        print(f'{key:>15}:  | {value:>7}')
    for arg in args:
        print(f'Деталі логів для рівня \'{arg.upper()}\':')
        logs = filter_logs_by_level(list_of_logs, arg.upper())
        dets = [f"{el['data']} {el['time']} - {el['message']}" for el in logs]
        print('\n'.join(dets))
    print('-'.join(['' for el in range(0, 35)]))

# for working in terminal:
#   you can write in terminal:
#       - python path_to_file
#       - python path_to_file info(debug and so on)

import sys
def find_terminal_arg():
    if len(sys.argv) > 1:
        return sys.argv[1]
terminal_arg = find_terminal_arg()

def main(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

if __name__ == '__main__':
    if terminal_arg:
        main(display_log_counts)(counted_by_level, terminal_arg)
    else:
        main(display_log_counts)(counted_by_level)


