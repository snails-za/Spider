class MyException(BaseException):
    def __init__(self, message):
        self.message = message


    def __str__(self):
        return self.message

    
    def haddle(self):
        print("问题已解决")

try:
    raise MyException("出现了异常")

except MyException as e:
    print(e)


raise MyException("异常")
