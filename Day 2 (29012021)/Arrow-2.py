def stars(number_of_stars):
    answer=''
    for i in range( number_of_stars ):
        answer+='*'
    answer=answer.center(30) #The center() method will center align the string,
        # using a specified character as the fill character.
    return answer

def arrow_head():
    for i in range(10):
        print (stars(i*2+1))

arrow_head()
