def solution(A):
    # write your code in Python 3.6
    n = len(A)
    min_list = [0]*n
    max_list = [0]*n
    for i in range(n):
        min_list[i] = i - A[i]
        max_list[i] = i + A[i]
    
    intersections, active_circles = 0, 0
    
    min_list.sort()
    max_list.sort()
    for i in range(n):
        if min_list[i] <= max_list[0]:
            #active_circles += 1 
            intersections += active_circles
            active_circles += 1
            #print("active_circles:",active_circles,"\nintersections:",intersections)
            
        else:
            max_list.pop(0)
            
            active_circles -=1
            intersections += active_circles
            #print("min_end_point:",max_list[0],"\nactive_circles:",active_circles,"\nintersections:",intersections)
    if intersections > 10e7:
        return -1
        
    else:
        return intersections

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    min_list = [0]*n
    max_list = [0]*n
    for i in range(n):
        min_list[i] = i - A[i]
        max_list[i] = i + A[i]
    
    intersections, active_circles = 0, 0
    
    min_list.sort()
    max_list.sort()
    print("min_list:",min_list,"\nmax_list:",max_list)
    i = 0
    while i in range(n):
        
        if min_list[i] <= max_list[0]:
            intersections += active_circles
            active_circles += 1
            print("active_circles:",active_circles,"\nintersections:",intersections)
            i += 1
        else:
            max_list.pop(0)
            active_circles -=1
            print("min_end_point:",max_list[0],"\nactive_circles:",active_circles,"\nintersections:",intersections)
    if intersections > 10e7:
        return -1
        
    else:
        return intersections

    

test_case = [1, 5, 2, 1, 4, 0]

answer = solution(test_case)

print(answer)