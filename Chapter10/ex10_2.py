#target date

import datetime
date=input("start day(yyyy-mm-dd) : ")
ymd=date.split('-')
startday=datetime.date(int(ymd[0]),int(ymd[1]),int(ymd[2]))

term=int(input("term(ex:-10,10) : "))
t=datetime.timedelta(days=100,hours=term)

print("target date is",(startday+t))
               
