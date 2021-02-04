def line_vert():
    for i in range (10):
        print("*")
def line_horz():
    answer=""
    for i in range (10):
        answer+="*"
    print(answer)

print("Example of two procedures called from within a program")
line_vert()
line_horz()
