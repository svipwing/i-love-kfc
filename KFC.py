import datetime,copy

def get_thursdays(year):
    thursdays = []
    d = datetime.date(year, 1, 1)
    while d.year == year:
        if d.weekday() == 3:
            thursdays.append(d)
        d += datetime.timedelta(days=1)
    return thursdays
    
def nextTime(day):
    ls = copy.deepcopy(day)
    weekday = 0
    count = 0
    while weekday!=3:
        try:
            day = day.replace(year=day.year + 1)
            count += 1
        except:
            day = day.replace(year=day.year + 4)
            count += 4
            
        weekday = day.weekday()
        
    say = f"{ls.month}月{ls.day}日 的 疯狂星期四，错过了要等 {count} 年！"
    return say

year = 2024

thursdays = get_thursdays(year)
ad = []

for thursday_date in thursdays:
    ad.append(nextTime(thursday_date))
    
for i in ad:
    print(i)
    print("")