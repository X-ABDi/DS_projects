from collections import deque

def find_steps(start, target):
    if start >= target:
        return start - target
    
    queue = deque([(start, 0)])  
    visited = set([start])  

    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        
        if current * 2 <= 2 * target and current * 2 not in visited:
            visited.add(current * 2)
            queue.append((current * 2, steps + 1))
        
        if current > 0 and current - 1 not in visited:
            visited.add(current - 1)
            queue.append((current - 1, steps + 1))

def main():
    inp = input().split()
    inp = list(int(i) for i in inp)
    result = find_steps(inp[0], inp[1])
    print(result)

main()
