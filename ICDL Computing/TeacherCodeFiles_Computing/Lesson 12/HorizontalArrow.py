def RepeatString( count, string ):
    result = ""
    for i in range( count ):
        result += string
    return result;

def LeftArrow( row, width):
    if( row < width ):
        stars = row+1
    else:
        stars = width*2+1-row
    return RepeatString( width+1-stars, " ") + RepeatString( stars, "*" )

def RightArrow( row, width):
    if( row < width ):
        stars = row+1
    else:
        stars = width*2+1-row
    return RepeatString( stars, "*") + RepeatString( width+1 - stars, " " )

def Shaft( row, height,length ):
    if( (row > height*0.25) and (row < height *0.75 )):
        string = RepeatString( length, "*" )
    else:
        string = RepeatString( length, " " )
    return string;

def Arrow( width, length ):
    for row in range( width*2+1):
        print( LeftArrow( row, width)  +
               Shaft( row, width*2, length) +
               RightArrow( row, width))

Arrow( 11, 45 )
