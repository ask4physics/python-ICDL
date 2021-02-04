# This function returns True if x is exactly divisible
# by divisor.  Otherwise it returns False.
def IsDivisibleBy( x, divisor ):
    return int(x/divisor)*divisor == x

for x in range(1,101):
    if( not IsDivisibleBy( x, 3 ) and not IsDivisibleBy( x, 5)):
        print( x )
    if( IsDivisibleBy( x, 3 ) and not IsDivisibleBy( x, 5)):
        print( "Fizz" )
    if( not IsDivisibleBy( x, 3 ) and IsDivisibleBy( x, 5)):
        print( "Buzz" )
    if( IsDivisibleBy( x, 3 ) and IsDivisibleBy( x, 5)):
        print( "FizzBuzz" )
        
        
    
