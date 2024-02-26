# FIXME: This is a workaround for the fact that we can'
# TODO: Remove this once we have a proper way to handle the


global_var = 10


def func(g_v):
    ans = 0
    for i in range(1_000_000_000):
            ans += i * g_v
            
    return ans 

# def func2():
#     ans = 0
#     for i in range(1_000_000_000):
#             ans += i * global_var
            
#     return ans 

print(func(global_var))
# print(func2())