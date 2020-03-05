kor,eng,mat,sci=98,77,85,90

def max_score(*args):
    return max(args)

maximum=max_score(kor,eng,mat)
print("maximum score :",maximum)

maximum=max_score(eng,mat,sci)
print("maximum score :",maximum)
