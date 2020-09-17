# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    base_array = [0] * n
    for query in queries:
        for i in range(n):
            if (query[0] <= i <= query[1]):
                base_array[i] = base_array[i] + query[2]
    return max(base_array)

    def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value


def Insert(head, data):
    if head == None:
        return Node(data, None)
    else:
        if head.next == None:
            head.next = Node(data,None)
        else:
            Insert(head.next,data)
        return head

class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

def insertNodeAtTail(head, data):
    if head == None:
        return Node(data)
    else:
        if head.next == None:
            head.next = Node(data)
        else:
            insertNodeAtTail(head.next, data)
        return head
