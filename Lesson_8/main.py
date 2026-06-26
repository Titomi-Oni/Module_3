# 1) Create two lists `numbers1` and `numbers2` containing integer values.
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# 2) Use `map()` with a `lambda` function to add corresponding elements:
#    a) The lambda takes two inputs `x` and `y`.
#    b) It returns `x + y`.
#    c) `map()` applies this to each pair from `numbers1` and `numbers2`
#       and stores the mapped result in `result`.
result = map(lambda x, y: x + y, numbers1, numbers2)
# 3) Print a heading message: "Addition of two lists".
print ("Addition of two lists")
# 4) Convert the `map` object into a list using `list(result)` and print the final added list.
print (list(result))
# 5) Create a list `nums` containing numbers to demonstrate `map()` again.
nums = [1,3,5,7]
def sq(n):
    return n*n
# 6) Define a function `sq(n)` that returns the square of a number (`n * n`).

# 7) Use `map(sq, nums)` to apply the `sq` function to every element in `nums`:
#    a) Convert the result into a list and store it in `square`.
square =  list(map(sq,nums))
# 8) Print a heading message: "Square of numbers in list"
#    and print the list `square`.
print ("Square of numbers in list")
print (square)