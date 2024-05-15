def hello():
    print("Greetings User")
hello()

def pack(arg1, arg2, arg3):
    return[arg1, arg2, arg3]
print(pack("a","b","c"))

def eat_lunch(food_list):
    if not food_list:
        print("my lunchbox is empty")
    else:
        print("first i eat", food_list[0])
        for food in food_list[1:]:
            print("next i eat", food)
eat_lunch(["sandwhich", "apple", "chips"])