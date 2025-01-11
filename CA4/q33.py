import queue

def depart_and_calculate(visited, graph, original_array, n_set, connected_set, start):
    bfs = queue.Queue()
    bfs.put(start)
    visited[start] = 1
    connected_set.add(start)
    n_set.add(original_array[start])
    while not bfs.empty():  
        node = bfs.get()
        for child in graph[node]:
            if visited[child] == 0: 
                bfs.put(child)  
                connected_set.add(child)
                n_set.add(original_array[child])
                visited[child] = 1

def main ():
    inp = list(map(int, input().split()))
    node_number = inp[0]
    graph = {}
    for i in range(1, node_number+1):
        graph[i] = set()
    original_array = list(map(int, input().split()))
    original_array.insert(0,0)
    for i in range(inp[1]):
        vertice = list(map(int, input().split()))
        graph[vertice[0]].add(vertice[1])
        graph[vertice[1]].add(vertice[0])
    visited = [0]*(node_number+1)
    connected_set = set() 
    sum = 0
    n_set = set()
    for i in range(1, node_number+1):
        if visited[i] == 0:
            depart_and_calculate(visited, graph, original_array, n_set, connected_set, i) 
            for _ in n_set & connected_set:
                sum += 1
            connected_set.clear()
            n_set.clear() 
    print(sum)                

    

main()