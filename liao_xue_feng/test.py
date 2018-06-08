import time, functools
def log(text):
    if isinstance (text, str):
        def log2(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('begin call' + text)
                res = fn(*args, **kw)
                print('end call')
        
            return wrapper
        return log2
    else:

        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call' )
            res = text(*args, **kw)
            print('end call')
        return wrapper

@log('gfre')
def f():
    print('执行')
    

@log
def m():
    print('执行')
    

f()
m()