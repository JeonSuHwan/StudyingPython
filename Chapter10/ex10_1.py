import datetime

today=datetime.date.today()
print("Today :",today)

date=input('end day(yyyy-mm-dd): ')
ymd=date.split('-')
endday=datetime.date(int(ymd[0]),int(ymd[1]),int(ymd[2]))

print(endday-today)
