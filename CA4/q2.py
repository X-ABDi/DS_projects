def add_eidi(tree, inp, wallets):
    wallets[inp[0]] += inp[1]
    if len(tree[inp[0]]) == 0:
        return
    for i in tree[inp[0]]:
        inp2 = [i, inp[1]]
        add_eidi(tree, inp2, wallets)

def main ():
    inp = input().split()
    inp = list(int(i) for i in inp)
    family_number = inp[0]
    year_number = inp[1]
    tree = [[]]
    wallets = []
    for i in range(family_number+1):
        wallets.append(0)
        tree.append([])
    for i in range(family_number-1):
        inp = input().split()
        inp = list(int(i) for i in inp) 
        tree[inp[0]].append(inp[1]) if inp[0] < inp[1] else tree[inp[1]].append(inp[0])  
    for i in range(year_number):
        inp = input().split()
        inp = list(int(i) for i in inp)
        add_eidi(tree, inp, wallets)
    del wallets[0]
    wallets = list(str(i) for i in wallets)
    answer = " ".join(wallets)
    print(answer)    

main()