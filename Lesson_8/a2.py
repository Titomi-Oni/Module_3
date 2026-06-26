# 1) Create two sets `s1` and `s2` with some elements.
s1 = {3, 6, 9}
s2 = {12,15,18}
# 2) Use `zip(s1, s2)` to pair elements from both sets position-wise:
#    a) Convert the zipped pairs into a list using `list(...)`
#    b) Store it in `s3`.
s3 = list(zip(s1,s2))
# 3) Print the list of zipped pairs `s3` and add a newline.
print (s3,"\n")
# 4) Create two lists `list1` and `list2` containing numbers.
list1 = [100, 200, 300 ]
list2 = [10, 20, 30]
# 5) Print paired elements where the second list is reversed:
#    a) Use `list2[::-1]` to reverse `list2`.
#    b) Use `zip(list1, list2[::-1])` to pair elements.
#    c) Loop through each pair as `x, y` and print them one by one.
for x, y in zip(list1, list2[::-1]):
    print (x,y)
# 6) Create two lists `stocks` and `prices` to demonstrate zipping into a dictionary.
stocks = ['Shopify','Red Bull', 'Nike']
prices = ['6556', '3756',' 8593']
# 7) Use dictionary comprehension with `zip(stocks, prices)`:
#    a) Each stock name becomes a key.
#    b) Each corresponding price becomes the value.
#    c) Store the result in `new_dict`.
new_dict = {stocks: prices 
            for stocks, prices in zip (stocks,prices)}
# 8) Print the final dictionary `new_dict` in a formatted way.
print (new_dict)