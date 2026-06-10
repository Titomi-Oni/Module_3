# 1) Create a tuple `tuplex` containing different data types (string, boolean, float, integer)
#    and print the tuple.
tuplex = ('Titomi', True, 5.8, 7)
print (tuplex)
# 2) Create another tuple `tuplex` containing only integer values and print it.
tuplex = (7, 8, 4, 6, 7, 3, 3)
print (tuplex)
# 3) Demonstrate tuple immutability:
#    a) Tuples cannot be modified directly (cannot add/change elements in the same tuple).
#    b) Use the`+` operator to merge tuples and create a new tuple.
#    c) Add a single element (9) using `(9,)` and store the new tuple back in `tuplex`.
#    d) Print the updated tuple.
tupley = tuplex + (9,)
print (tupley)
# 4) Create a tuple `tuple1` and count occurrences of a specific value:
#    a) Use `tuple1.count(50)` to count how many times 50 appears.
#    b) Print the count.
print (tuplex.count(7))
# 5) Create a tuple `tuplex` with multiple integers to demonstrate slicing.
# 6) Slice a portion of the tuple using indexing:
#    a) Use `tuplex[3:5]` to get elements from index 3 up to index 4 (stop index is excluded).
#    b) Store it in `_slice` and print it.
print (tuplex[3:5])
# 7) Slice from the beginning when the start index is not provided:
#    a) Use `tuplex[:6]` to get elements from index 0 up to index 5.
#    b) Store it in `_slice` and print it.
print (tuplex[:6])