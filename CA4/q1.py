import math

def find_steps(inp, answer):
    if (inp[0] > inp[1]):
        answer[0] += inp[0]-inp[1]
        return
    elif (inp[0] == inp[1]):
        return
    else:
        if 2*inp[0] > inp[1]:
            answer[0] += 1+math.ceil((2*inp[0]-inp[1])/2)
            return 
        else:
            inp[0] = 2*inp[0]
            answer[0] += 1
            find_steps(inp, answer)


def main ():
    inp = input().split()
    inp = list(int(i) for i in inp)
    answer = [0]
    find_steps(inp, answer)
    print(answer[0])

main()