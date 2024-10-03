from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        current_date = datetime.today().date()
        
        delta = (target_date - current_date).days
        
        return delta

    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

days_difference = get_days_from_today("2021-10-09")
print(f"Кількість днів між сьогоднішньою датою і заданою: {days_difference}")