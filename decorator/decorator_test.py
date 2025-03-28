##nested functions....function returning function


def smart_divide(func):
    print('inside decorator')

    def inner(a, b):
        print('inside inner')
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)   ##function calling itself


    print("outside inner")
    return inner  ##returning function which invokes inner method


@smart_divide    #decorator call
def divide(a, b):
    print('inside divide')
    print(a/b)


# divide(2,5)
divide(2,0)



