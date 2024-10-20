import sys

def main ():
    i = input()
    i.strip()    
    output = "" 
    sign = "" 
    if i[0] == '+' or i[0] == '-':
        sign = i[0]
        i = i[1:]
       
    for j in range(0, len(i)):
        if i[j].isdigit():
            output += i[j] 
        else:
            break       
    if output == "":
        print(0)
    elif int(output) > sys.maxsize and sign == '+':
        print(sys.maxsize)
    elif int(output) > sys.maxsize and sign == '-':
        print(-sys.maxsize - 1)        
    else:
        print(sign,int(output), sep="")    
    
       
main ()