from data import data, signs
import datetime

def get_current_year():
    today = datetime.date.today()
    return  today.year


def get_sign(day, month):
    year = get_current_year()
    birthday = datetime.date(year, month, day)
    
    for sign in signs:
        period = signs[sign]
        if period["start"] <= birthday <= period["end"]:
            return sign
    