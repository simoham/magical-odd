from bottle import route, run, template, jinja2_template, jinja2_view
from magical import generate_magic_square_odd
import json

@route('/magic/<dim:int>')
@jinja2_view('index.html')
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

run(host='localhost', port=8080)
