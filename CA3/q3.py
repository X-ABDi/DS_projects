def main ():
    n = int(input())
    point_dic = {}
    while n > 0:
        l = list(input().split())
        l = list(int(el) for el in l)
        
        keys = point_dic.keys()
        if l[0] in range(1, 1+n) and l[0] in keys:
            point_dic[l[0]] += 1
        elif l[0] in range(1, 1+n) and l[0] not in keys:
            point_dic[l[0]] = 1 

        if l[1] in range(1, 1+n) and l[1] in keys:
            point_dic[l[1]] += 1
        elif l[1] in range(1, 1+n) and l[1] not in keys:
            point_dic[l[1]] = 1     

        n -= 1

    values = point_dic.values()
    for value in values:
        print(value)
        if value == values[-1]:
            print('\n', end="")
        else:
            print(" ", end="")    

main ()