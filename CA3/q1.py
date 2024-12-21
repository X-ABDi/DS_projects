import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self, value):
            self.value = value
            self.index = 0

    def __init__(self):
        self.arr = []

    def bubble_up(self, index):
        if len(self.arr) == 0:
            raise Exception (EMPTY)
        elif index >= len(self.arr) or index < 0:
            raise Exception (OUT_OF_RANGE_INDEX)
        try:
            index = int(index)
        except ValueError:
            raise Exception (INVALID_INDEX)  
        if index == 0:
            return  

        if index%2 == 0:
            parent = index//2 - 1
        else:
            parent = index // 2 
        if parent >= 0:    
            if self.arr[parent].value > self.arr[index].value:
                self.arr[parent].value , self.arr[index].value = self.arr[index].value , self.arr[parent].value    
                self.bubble_up(parent)
        else:
            return        


    def bubble_down(self, index):
        if (len(self.arr)) == 0:
            raise Exception (EMPTY)
        elif index >= len(self.arr) or index < 0:
            raise Exception (OUT_OF_RANGE_INDEX)
        try:
            index = int(index)
        except ValueError:
            raise Exception (INVALID_INDEX)
        
        least = index
        if (2*index+1) < len(self.arr) and self.arr[2*index+1] < self.arr[least]:
            least = 2*least+1
        if (2*index+2) < len(self.arr) and self.arr[2*index+2] < self.arr[least]:
            least = 2*index+2
        if least != index:
            self.arr[index].value , self.arr[least].value = self.arr[least].value , self.arr[index].value
            self.bubble_down(least)         


    def heap_push(self, value):
        node = self.Node()
        node.value = value
        node.index = len(self.arr)
        self.arr.append(node)
        self.bubble_up(node.index)

    def heap_pop(self):
        if len(self.arr) == 0:
            raise Exception (EMPTY)
        if len(self.arr) == 1:
            last = self.arr[-1]
            self.arr.pop()
            return last
        last = self.arr[0]
        self.arr[0].value , self.arr[-1].value = self.arr[-1].value , self.arr[0].value
        self.arr.pop()
        self.bubble_down(0)
        return last

    def find_min_child(self, index):
        if len(self.arr) == 0:
            raise Exception (EMPTY)
        elif index < 0 or index >= len(self.arr):
            raise Exception (OUT_OF_RANGE_INDEX)
        try:
            index = int(index)
        except ValueError:
            raise Exception (INVALID_INDEX)
        
        if 2*index+1 > len(self.arr):
            raise Exception ('no child')
        elif 2*index+2 > len(self.arr):
            return self.arr[2*index+2]
        else:
            return self.arr[2*index+1] if self.arr[2*index+1] < self.arr[2*index+2] else self.arr[2*index+2]


    def heapify(self, *args):
        for val in args:
            node = self.Node()
            node.value = val
            self.arr.append(node)
            self.bubble_up(len(self.arr)-1)



class HuffmanTree:
    class Node:
        def __init__(self):
            self.freq = 0
            self.value = ""
            self.code = []
            self.children = []

    def __init__(self):
        self.arr = []
        self.tree = self.Node()

    def set_letters(self, *args):
        if len(self.arr) == 0:
            for letter in args:
                node = self.Node()
                node.value = letter
                self.arr.append(node)
        else:
            index = 0
            for letter in args:
                if self.arr[index] != None:
                    self.arr[index].value = letter
                    index += 1
                    

    def set_repetitions(self, *args):
        if len(self.arr) == 0:
            for freq in args:
                node = self.Node()
                node.freq = freq
                self.arr.append(node)
        else:
            index = 0
            for freq in args:
                if self.arr[index] != None:
                    self.arr[index].freq = freq
                    index += 1



    def set_text(self, text):
        if len(text) == 0:
            raise Exception (EMPTY)
        huffman_dic = {}
        for letter in text:
            if letter in huffman_dic:
                huffman_dic[letter] += 1
            else:
                huffman_dic[letter] = 1
        for value, freq in huffman_dic.items():
            node = self.Node()
            node.value = value
            node.freq = freq
            self.arr.append(node)        

    def bubble_sort(self, temp_arr):
        if len(temp_arr) <= 1:
            return
        for i in range(len(temp_arr)-1, 0, -1):
            if temp_arr[i].freq > temp_arr[i-1].freq:
                temp_arr[i], temp_arr[i-1] = temp_arr[i-1], temp_arr[i]
            else:
                break    

    def build_tree(self):
        if len(self.arr) == 0:
            raise Exception(EMPTY)
        
        self.arr.sort(key=lambda node : node.freq, reverse=True)
        temp_arr = self.arr.copy()
        while len(temp_arr) >= 1:
            node = self.Node()
            node.freq = temp_arr[-1].freq + temp_arr[-2].freq
            node.value = ""
            node.children = [temp_arr[-2], temp_arr[-1]]
            temp_arr.pop()
            temp_arr.pop()
            temp_arr.append(node)
            self.bubble_sort(temp_arr)

        self.tree = temp_arr[0]    

    def set_code(self ,node , code, comp_code):
        if len(node.children) == 0:  # save code for each node in arr.  upload to github
            comp_code += node.freq*len(code)
            return
        left_code = code + [0]
        node.children[0].code = left_code
        right_code = code + [1]
        node.children[1].code = right_code
        self.set_code(node.children[0], left_code)
        self.set_code(node.children[1], right_code)
            

    def get_compressed_length(self):
        node = self.tree
        comp_code = 0
        code = []
        self.set_code(node, code, comp_code)
        return comp_code


class Bst:
    SENTINEL = object()
    class Node:
        def __init__(self):
            self.key = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = self.Node()

    def insert(self, key):
        node = self.root
        while node != None:
            if node.key == None:
                node.key = key
                break   
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left

        node = self.Node()
        node.key = key
        node.left = None
        node.right = None            

    
    def preorder(self, node=SENTINEL):
        if node is self.SENTINEL:
            node = self.root
        if node is None:
            return ""
        str_left = self.preorder(node.left)  
        str_right = self.preorder(node.right)
        return str_left + str(node.key) + str_right

    def inorder(self,node=SENTINEL):
        if node is self.SENTINEL:
            node = self.root
        if node is None:
            return ""
        str_left = self.preorder(node.left)  
        str_right = self.preorder(node.right)
        return str(node.key) + str_left + str_right

    def postorder(self, node=SENTINEL):
        if node is self.SENTINEL:
            node = self.root
        if node is None:
            return ""
        str_left = self.preorder(node.left)  
        str_right = self.preorder(node.right)
        return str_left + str_right + str(node.key)


class Runner:
    ds_map = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()

        args = [x.strip() for x in args_list.split(',')] if args_list != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[item_name], func_name)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
