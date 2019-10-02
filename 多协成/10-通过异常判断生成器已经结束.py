

def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a+b
        current_num += 1
    return "ok----"

# 如果在调用_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
b = create_num(2)


while True:
    try:
        ret = next(b)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break

# for i in a:
#     print(i)











