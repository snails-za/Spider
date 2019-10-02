

def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    
    while current_num < all_num:
        # print(a)
        ret = yield a  
        print("-->>>ret>>>", ret)
        a, b = b, a+b
        current_num += 1

obj = create_num(10)

ret = next(obj)
print(ret)

ret = obj.send(8)
print(ret)









