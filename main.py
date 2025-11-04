from datetime import datetime


def parse_moscow_times(date):
    try:
        return datetime.strptime(date, '%A, %B %d, %Y')
    except ValueError:
        return None


def parse_guardian(date):
    try:
        return datetime.strptime(date, '%A, %d.%m.%y')
    except ValueError:
        return None


def parse_daily_news(date):
    try:
        return datetime.strptime(date, '%A, %d %B %Y')
    except ValueError:
        return None


def parse_date(date):
    parsers = [
        parse_moscow_times,
        parse_guardian,
        parse_daily_news
    ]
    for parser in parsers:
        result = parser(date)
        if result:
            return result

    return None


def main():
    user_input = input("Введите дату или q, чтобы выйти: ")
    while user_input != "q":
        date_obj = parse_date(user_input)
        if date_obj:
            print(f"Объект datetime: {date_obj}")
            user_input = input("Введите дату или q, чтобы выйти:\n")
        else:
            user_input = input("Введите дату или q, чтобы выйти:\n")


if __name__ == "__main__":
    main()
