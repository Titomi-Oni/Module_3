def square_values(start,end):
    squares = []
    even_squares = []
    odd_squares = []

    for n in range (start, end + 1):
        sq = n ** 2
        if sq % 2 ==0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)

    print ("All Squares:",squares)
    print ("All Even Squares:",even_squares)
    print ("All Odd Squares:",odd_squares)

    return squares, even_squares, odd_squares

square_values(1,10)