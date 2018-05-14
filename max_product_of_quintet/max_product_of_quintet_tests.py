from max_product_of_quintet import max_product_of_quintet

raised = False
try:
    max_product_of_quintet([])
except:
    raised = True

assert raised, 'Exception (< 5 numbers) expected, but not raised'

# ---

raised = False
try:
    max_product_of_quintet([1,2,3,4])
except:
    raised = True

assert raised, 'Exception (< 5 numbers) expected, but not raised'

# ---

assert max_product_of_quintet([-1,-3,3,2,-6,-5,7]) == 1260
assert max_product_of_quintet([1,2,3,4,5]) == 120
assert max_product_of_quintet([-1,2,2,4,4]) == -64
assert max_product_of_quintet([-10,-20,-30,-40,-50, 0]) == 0
assert max_product_of_quintet([-10,0,2,4,6,8]) == 0
assert max_product_of_quintet([-1,-100,0,20,40,60,80]) == 0
# print(max_product_of_quintet([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]))

assert max_product_of_quintet([-1,1,-1,1,-1]) == -1
assert max_product_of_quintet([0,0,0,0,0]) == 0