def hello():
    print("howdy person")


def pack(a, b, c):
    return [a, b, c]


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("what lunch")
    else:
        print("First I eat " + lunch_list[0])
        for i in lunch_list[1:]:
            print('next I eat ' + i)


lunch = ['avacado', 'beans', 'mango']
lunch2 = ['booberries']
hello()
print(pack(1, 3, lunch))
eat_lunch(lunch)
eat_lunch(lunch2)
