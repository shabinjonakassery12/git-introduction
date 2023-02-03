def all(*args, **kwargs):
    print(args)
    print("helooo")
    print(kwargs)



'''courses = ['science', 'maths','cs']
info = {'name': 'John', 'age':21}

all(*courses, **info)'''



'''def is_leap(year):
    return year % 4 == 0 and (year % 100 == 0 or year % 400 == 0)


year = 2001
print(is_leap(year))'''


print("MY  MODULE IMPORTED")
test = 'my test module'
abc = 'my abc'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1
