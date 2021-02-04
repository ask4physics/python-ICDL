def stars(number_of_stars):
    answer=''
    for i in range( number_of_stars ):
        answer+='*'
    answer=answer.center(30)
    return answer

print( stars(1) )
print( stars(3) )
print( stars(5) )
