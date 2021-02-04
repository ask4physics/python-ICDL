def stars(number_of_stars):
    answer=''
    for i in range( number_of_stars ):
        answer+='*'
    answer=answer.center(30) #The center() method will center align the string,
        # using a specified character as the fill character.
    return answer

print( stars(1) )
print( stars(3) )
print( stars(5) )
print( stars(7) )
print( stars(9) )
print( stars(11) )
