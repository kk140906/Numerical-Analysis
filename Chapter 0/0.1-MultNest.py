# 嵌套乘法计算：可以尽可能使计算机进行简单计算，加快运行效率
# 对于y = c1 + c2 * x + c3 * x^2 + c4 * x^3的多项式，
# 改写为一般的嵌套乘法公式 ：
# y = c1 + (x - r1) * (c2 + (x - r2) * (c3 + (x - r3) * c4)))
# r1 r2 r3 r4 称为基点
import numpy as np
import time
def multNest(x:float,n:int,c:list,r:list):
    """x - value x;\n
       n - polynomial order;\n
       c - polynomial coefficient;\n
       r - base point."""
    cii = c[-1] 
    for ci,ri in zip(c[:-1][::-1],r[::-1]):
        cii = ci + (x - ri) * cii 
        yield cii

def genCoefflist(assigncoeff:dict):
    """"assigncoeff - dict {keys:values};\n
        keys - polynomial order,constant's order is 0;\n
        values - polynomial coefficient."""
    order = max([int(key) for key in assigncoeff.keys()])
    coefflist = np.zeros((order + 1,))
    for coeff in assigncoeff:
        coefflist[int(coeff)] = assigncoeff[coeff]
    return coefflist,order

# test 1 例0.1
print("Example 0.1:")
coeff,order = genCoefflist({"5":4,"8":7,"11":-3,"14":2})
test = multNest(0.5,order,coeff,np.zeros_like(coeff))
for i in range(order):
    y=next(test)
print("y =",y)

# test 2 编程问题1 
print("Code 0.1:")
test = multNest(1.00001,50,np.ones((51,)),np.zeros((50,)))
for i in range(50):
    y=next(test)
q = (1.00001 ** 51 -1) / (1.00001 -1)
print("y = {}\nq = {}\nerror = {}".format(y,q,y-q))    
