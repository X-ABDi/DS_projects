class minHeap:
    def __init__(self):
        self.min_arr = []

    def bubbleUp(self):
        num = len(self.min_arr)-1
        while num != 0:
            if num%2 == 0:
                parent = num//2 - 1
            else:
                parent = num // 2 

            if self.min_arr[num] < self.min_arr[parent]:
                self.min_arr[num] , self.min_arr[parent] = self.min_arr[parent] , self.min_arr[num]
                num = parent
            else:
                break    

    def bubbleDown(self):
        num = 0
        while num != len(self.min_arr):
            least = num
            left_child = 2*num+1
            right_child = 2*num+2
            if left_child < len(self.min_arr) and self.min_arr[least] > self.min_arr[left_child]:
                least = left_child
            if right_child < len(self.min_arr) and self.min_arr[least] > self.min_arr[right_child]:
                least = right_child
            if least != num:
                self.min_arr[num], self.min_arr[least] = self.min_arr[least], self.min_arr[num]
                num = least
            else:
                break        

    def insert(self, n):
        self.min_arr.append(n)
        self.bubbleUp()

    def delete(self):
        self.min_arr[0] , self.min_arr[-1] = self.min_arr[-1] , self.min_arr[0]
        self.min_arr.pop()
        self.bubbleDown()    

class maxHeap:
    def __init__(self):
        self.max_arr = []

    def bubbleUp(self):
        num = len(self.max_arr)-1
        while num != 0:
            if num%2 == 0:
                parent = num//2 - 1
            else:
                parent = num // 2 

            if self.max_arr[num] > self.max_arr[parent]:
                self.max_arr[num] , self.max_arr[parent] = self.max_arr[parent] , self.max_arr[num]
                num = parent
            else:
                break    

    def bubbleDown(self):
        num = 0
        while num != len(self.max_arr):
            greatest = num
            left_child = 2*num+1
            right_child = 2*num+2
            if left_child < len(self.max_arr) and self.max_arr[greatest] < self.max_arr[left_child]:
                greatest = left_child
            if right_child < len(self.max_arr) and self.max_arr[greatest] < self.max_arr[right_child]:
                greatest = right_child
            if greatest != num:
                self.max_arr[num], self.max_arr[greatest] = self.max_arr[greatest], self.max_arr[num]
                num = greatest
            else:
                break

    def insert(self, n):
        self.max_arr.append(n)
        self.bubbleUp()  

    def delete(self):
        self.min_arr[0] , self.min_arr[-1] = self.min_arr[-1] , self.min_arr[0]
        self.min_arr.pop()
        self.bubbleDown()              

def main ():
    max_heap = maxHeap()
    min_heap = minHeap()
    t = int(input())
    while t != 0:
        n = int(input())
        if n == 0:
            min_heap.min_arr = []
            max_heap.max_arr = []
            t -= 1
        elif n == -1:
            if len(min_heap.min_arr) > len(max_heap.max_arr):
                print(min_heap.min_arr[0])
                min_heap.delete()
            elif len(max_heap.max_arr) > len(min_heap.min_arr):
                print(max_heap.max_arr[0])
                max_heap.delete()
            else:
                if max_heap.max_arr[0] < min_heap.min_arr[0]:
                    print(max_heap.max_arr[0])
                    max_heap.delete()
                else:
                    print(min_heap.min_arr[0])
                    min_heap.delete()      
        else:    
            if len(min_heap.min_arr) == 0 and len(max_heap.max_arr) == 0:
                min_heap.min_arr.insert(n)

            elif len(min_heap.min_arr) > len(max_heap.max_arr):
                if n <= min_heap.min_arr[0]:
                    max_heap.max_arr.insert(n)
                else:
                    min_heap.min_arr.insert(n)  
                    max_heap.max_arr.insert(min_heap.min_arr[0])
                    min_heap.delete()
            elif len(min_heap.min_arr) < len(max_heap.max_arr):
                if n >= max_heap.max_arr[0]:
                    min_heap.insert(n)
                else:
                    max_heap.max_arr.insert(n)
                    min_heap.min_arr.insert[max_heap.max_arr[0]]
                    max_heap.delete()
            elif (min_heap.min_arr[0] < max_heap.max_arr[0] and n < min_heap.min_arr[0]) or (min_heap.min_arr[0] > max_heap.max_arr[0] and n < max_heap.max_arr[0]):
                max_heap.max_arr.insert(n)
            elif (min_heap.min_arr[0] >= max_heap.max_arr[0] and n >= max_heap.max_arr[0]) or (min_heap.min_arr[0] <= max_heap.max_arr[0] and n >= min_heap.min_arr[0]):  
                min_heap.min_arr.insert(n)  


main()    