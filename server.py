from bottle import route, run, template, jinja2_template, jinja2_view
from magical import generate_magic_square_odd
from pascal import pascals_triangle
from fibo import fibonacci_triangle

import json, platform, time

@route('/magic/<dim:int>')
@jinja2_view('index.html')
def index(dim):

    if dim % 2 == 0 :
        return "Doesnt work for even"

    start_time = time.perf_counter()
    square = generate_magic_square_odd(dim)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Magic Square of order {dim}:\n{square}")

    # The magic constant (sum of rows/cols/diagonals) can be verified:
    magic_constant = dim * (dim**2 + 1) // 2
    print(f"\nMagic Constant: {magic_constant}")

    #return template('{{square}}!', square=square)
    message = {"magic":square.tolist()}
    return {'message':message, 'n':dim, 'hostname':platform.node(), 'time':elapsed_time}

@route('/magic/json/<dim:int>')
def index(dim):

    if dim % 2 == 0 :
        return "Doesnt work for even"

    square = generate_magic_square_odd(dim)
    print(f"Magic Square of order {dim}:\n{square}")

    # The magic constant (sum of rows/cols/diagonals) can be verified:
    magic_constant = dim * (dim**2 + 1) // 2
    print(f"\nMagic Constant: {magic_constant}")

    #return template('{{square}}!', square=square)
    message = {"magic":square.tolist()}
    return {'message':message, 'n':dim}


@route('/triangle/pascal/<n:int>')
@jinja2_view('pascal.html')
def index(n):
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    triangle = pascals_triangle(n)
    elapsed_time = end_time - start_time

    tr=""
    for i, row in enumerate(triangle):
      spaces = " " * (n - i) * 2
      tr+=spaces + "   ".join(map(str, row))+"<br>"

    return {"triangle":tr, "hostname":platform.node(), "time":elapsed_time, "n":n}

@route('/triangle/fibonacci/<n:int>')
@jinja2_view('fibonacci.html')
def index(n):
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    triangle = fibonacci_triangle(n)
    elapsed_time = end_time - start_time

    return {"triangle":triangle, "hostname":platform.node(), "time":elapsed_time, "n":n}


run(host='0.0.0.0', port=8080)

