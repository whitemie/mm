def log(fun):
    def func1(*args):
        print("----log日志打印开始---")
        fun(*args)
        print("----log日志打印结束---")
    return func1

@log
def add(a,b,c):

    print("a+b+c的结果是{}".format(a+b+c))

add(1,2,3)