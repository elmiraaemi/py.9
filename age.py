from datetime import date, datetime
import datetime
from khayyam import JalaliDate, JalaliDatetime
user_birthday = input("1999-01-28 \t")
birthday_year = int(user_birthday.split("-")[0])
birthday_month = int(user_birthday.split("-")[1])
birthday_day = int(user_birthday.split("-")[2])
milai = JalaliDatetime(birthday_year, birthday_month, birthday_day).todate()
dob = str(milai)
dob_date = datetime.date.fromisoformat(dob)
today_date = datetime.date.today()
age_timedelta = today_date - dob_date
age_days = age_timedelta.days
age_years = age_days // 365
day2 = age_days - age_years*365
age_month = day2 // 30
month2=day2%30
print(age_years,age_month,month2)



# # miladi
# import datetime
# dob = input("1999-01-28 \t")
# dob_date = datetime.date.fromisoformat(dob)
# today_date = datetime.date.today()
# age_timedelta = today_date - dob_date
# age_days=age_timedelta.days
# age_years=age_days // 365
# age_month=(age_days % 365) // 30
# print(age_years,age_month,age_days)