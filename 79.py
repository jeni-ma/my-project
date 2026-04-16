def wrapper(f):
    def fun(l):
    
        formatted_list = [f"+91 {num[-10:-5]} {num[-5:]}" for num in l]
        return f(formatted_list)
    return fun

