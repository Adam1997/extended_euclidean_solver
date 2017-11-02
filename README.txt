This is a Python project to solve Extended Euclidean Algorithm Problems.

The program uses an algorithm to solve for x and y such that ax + by = gcd(x, y)
The algorithm works using Linear Algebra and matrix multiplication.
For each recursive call of gcd(x,y), the quotient of x/y is recorded.
These quotients are then turned into Matrices (represented by the Matrix custom class) of the form:
{0    1}
{1   qk}

where qk is the quotient of the kth recursion call

Another matrix (say m1), defined by
{0   1}
{1   0}
is then created.

Then m1.q1 is multiplied to give the following matrix:
{1  qk}
{0   1}

This matrix then multiplies the next quotient matrix and so on.

The second last matrix is defined by:

{a   x}
{b   y}
where a and b are constants and x, y are the solutions to the Euclidean equation.

The program then figures out whether x is negative or if y is negative and matches these to the correct
coefficients. (THIS MATCHING PART IS A WIP)

To be added:
- exceptions
- checks
- improved matching Algorithm
- more constructors
- user input
- more comprehensive matrix class (adding other matrix operations other than multiplication)
