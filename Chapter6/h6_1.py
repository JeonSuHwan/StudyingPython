engdict={'1':'one','2':'two','3':'three','4':'four','5':'five'}
spandict={'1':'uno','2':'dos','3':'trois','4':'cuatro','5':'cinq'}
frendict={'1':'un(e)','2':'deux','3':'tres','4':'quatre','5':'cinco'}
title=('English','Spanish','French')

while True:
    num=input("Please enter a number (1~5) : ")
    if num==1:
        for i in title:
            if i=='English':
                print("{} : {}".format(i,engdict[num]))
            elif i=='Spanish':
                print("{} : {}".format(i,spandict[num]))
            else:
                print("{} : {}".format(i,spandict[num]))
    elif num==2:
        for i in title:
            if i=='English':
                print("{} : {}".format(i,engdict[num]))
            elif i=='Spanish':
                print("{} : {}".format(i,spandict[num]))
            else:
                print("{} : {}".format(i,spandict[num]))
    elif num==3:
        for i in title:
            if i=='English':
                print("{} : {}".format(i,engdict[num]))
            elif i=='Spanish':
                print("{} : {}".format(i,spandict[num]))
            else:
                print("{} : {}".format(i,spandict[num]))
    elif num==4:
        for i in title:
            if i=='English':
                print("{} : {}".format(i,engdict[num]))
            elif i=='Spanish':
                print("{} : {}".format(i,spandict[num]))
            else:
                print("{} : {}".format(i,spandict[num]))
    elif num==5:
        for i in title:
            if i=='English':
                print("{} : {}".format(i,engdict[num]))
            elif i=='Spanish':
                print("{} : {}".format(i,spandict[num]))
            else:
                print("{} : {}".format(i,spandict[num]))
    elif num=='': #if you input enter key, program is terminated.
        break
    else:
        print("Try again!")
