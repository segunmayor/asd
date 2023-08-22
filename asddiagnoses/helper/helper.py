from datetime import date, datetime

def getCurrentDate():
    today = date.today()
    return today

def getCurrentAgeOfGuardian(dob):
    today = getCurrentDate()
    age = today.year - datetime.strptime(dob, '%Y-%m-%d').year
    return age