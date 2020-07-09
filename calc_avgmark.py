def fun(name,*marks):
    total = 0
    for mark in marks:
        total += mark
    subjects = len(marks)
    avg_mark = total/subjects
    print(name," - ",avg_mark)


fun("preetha",80,96,84,70,56)