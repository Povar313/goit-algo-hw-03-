from datetime import datetime

def get_days_from_today(date):

    target_date = datetime.strptime(date, '%Y-%m-%d')

    current_date = datetime.today()

    delta = (target_date - current_date).days

    return delta


days_difference = get_days_from_today("2021-10-09")

print("Кількість днів між сьогоднішньою датою і заданою:", days_difference)