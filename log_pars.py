import collections
import sys
from pathlib import Path


def parse_log_line(line: str) -> dict:
    ''' для парсингу рядків логу
    яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. '''
    parts = line.strip().split()

    date = parts[0]
    time = parts[1]
    level = parts[2]

    msg = ' '.join(parts[3:])

    return {
        'date': date,
        'time': time,
        'level': level,
        'messege': msg
    }


def load_logs(file_path: str) -> list:
    ''' для завантаження логів з файлу '''
    logs = []
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                logs.append(parsed_line)

    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено!")
        return None

    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return None

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    ''' для фільтрації логів за рівнем '''
    return [log for log in logs if log['level'].upper() == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    ''' для підрахунку записів за рівнем логування '''
    unique_level_count = collections.Counter([log['level'] for log in logs])
    unique_dict = dict(unique_level_count)
    return unique_dict


def display_log_counts(counts: dict):
    ''' яка форматує та виводить результати.
    Вона приймає результати виконання функції count_logs_by_level '''
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f'{level:<16} | {count}')


def main():
    # file_path = Path(r'C:\Projects_GoIT\goit-algo-hw-05\logfile.log')

    file_path = sys.argv[1]

    if not Path(file_path).exists():
        print(f"Помилка: Файл '{file_path}' не існує!")
        return

    logs = load_logs(file_path)
    if logs is None:
        return

    if not logs:
        print("Файл порожній або не містить валідних записів!")
        return

    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if len(sys.argv) > 2:
        level_filter = sys.argv[2].upper()

        filtered_logs = filter_logs_by_level(logs, level_filter)

        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['messege']}")
        else:
            print(f"\nНемає записів для рівня '{level_filter}'")


if __name__ == '__main__':
    main()
