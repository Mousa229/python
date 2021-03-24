#the code with no fonction of square bequse the function f square is from our own making so we can import it from
# the previas file   and the error is (name 'square' is not defined)
# and the code [from functions import square] will solve the problem.

from functions import square

for i in range(10):

    print(f"The square of {i} is = {square(i)}")
#Note : That you can make your own functions in files and you can yse thim to solv problems.
