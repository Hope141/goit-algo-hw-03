from datetime import datetime

def get_days_from_today(date):
    try:
        string_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_day = datetime.today().date()
        return (current_day - string_date).days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

print(get_days_from_today("2020-10-09")) 
print(get_days_from_today("2025-01-01"))