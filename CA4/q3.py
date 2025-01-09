import queue

def depart_and_calculate(visited, graph, connected_set, node_number, start):
    visited[start] = 1
    bfs = queue.Queue()
    bfs.put(start)
    connected_set.append(start)
    while not bfs.empty():  
        node = bfs.get()
        for i in range(1, node_number+1):
            if graph[node][i] == 1:
                if visited[i] == 0:
                    bfs.put(i)
                    connected_set.append(i)
                    visited[i] = 1

def main ():
    inp = input().split()
    inp = list(int(i) for i in inp)
    node_number = inp[0]
    graph = [[0 for _ in range(inp[0]+1)] for _ in range(inp[0]+1)]
    original_array = input().split()
    original_array = list(int(i) for i in original_array)
    original_array.insert(0,0)
    for i in range(inp[1]):
        vertice = input().split()
        vertice = list(int(j) for j in vertice)
        graph[vertice[0]][vertice[1]] = 1
        graph[vertice[1]][vertice[0]] = 1
    visited = [0]*(node_number+1)
    connected_set = [] 
    sum = 0
    n_set = []
    for i in range(1, node_number+1):
        if visited[i] == 0:
            depart_and_calculate(visited, graph, connected_set, node_number, i) 
            for node in connected_set:
                n_set.append(original_array[node])
            for node in connected_set:
                if node in n_set:
                    sum += 1
            connected_set = []
            n_set = []    
    print(sum)                

    

main()