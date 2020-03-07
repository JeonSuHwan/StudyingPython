import random

#make list
def dataInput():
    data=input("data list(ex:a,b,c) : ")
    return data.split(',')

#shuffle list
def shake(list):
    random.shuffle(list)
    return list
