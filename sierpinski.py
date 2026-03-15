def sierpinski_triangle(n):
    """Generate Sierpinski triangle pattern using binary representation"""
    row = ""
    for i in range(n):
        # Calculate binary representation pattern
        for j in range(n - i):
            row += " "
        for j in range(i + 1):
            if i & j == j:  # Sierpinski condition
                row += "▲ "
            else:
                row += "  "
        row +="\n"

    return row

a=sierpinski_triangle(60)
print(a)
