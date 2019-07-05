# 两分法
# 根据中值定理,函数f(x)在区间[a,b]内满足f(a) * f(b) <= 0,则必定存在一个值r满足f(r) = 0;
# 为简化例子，此方法在使用中假设函数在所求区间内单调且连续；
# 书中通过评估上下两个区间的范围差值的中值小于容差,本代码中通过评估函数值小于容差,两者结果相近，存在一定误差
import math
def dichotomy(scope, func,toloerance):
    lower = scope[0]
    upper = scope[1]
    result_lower = func(lower)
    result_upper = func(upper)
    if result_lower * result_upper > 0:
        return
    mid = (lower + upper) / 2
    result = func(mid)
    count = 1
    while abs(result) >= toloerance:
        if result * result_lower < 0:
            upper = mid
        else:
            lower = mid
        mid = (lower + upper) / 2
        result = func(mid)
        if not result:
            break
        count = count + 1
    print(count)
    return mid


scope = [0, 1]
# f = lambda x: x ** 3 + x - 1
f = lambda x: math.cos(x) - x
result = dichotomy(scope, f, 1e-6)
print('{:.6f}'.format(result))
