class cell:

    def __init__(self, x = 0, y=0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x,y,N):
    """checks whether given position is inside the board

    Args:
        x (int): x coordinate of the position
        y (int): y coordinate of the position
        N (int): maxlength of the board
    """ 
    if (x >= 1 and x <=N and y >= 1 and y <= N):
        return True
    return False

def minStepToReachTarget(knightpos, targetpos, N):
    """method returns minimum step to reach target position

    Args:
        knightpos (list): list of starting coordinates
        targetpos (list): list of target coordinates
        N (int): max length of the board
    """    
    #all possible movement for the knight
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    queue = []

    #push starting position of knight with 0 distance
    queue.append(cell(knightpos[0], knightpos[1],0))

    #make all cell univisted
    visited = [[False for i in range(N+1)] for j in range(N+1)]

    #visit starting state
    visited[knightpos[0]][knightpos[1]] = True

    #loop until we have one element in queue
    while(len(queue) > 0):
        t = queue[0]
        queue.pop(0)

        if(t.x == targetpos[0] and t.y == targetpos[1]):
            return t.dist
        
        #iterate for all reachable states
        for i in range(8):

            x = t.x + dx[i]
            y = t.y + dy[i]

            if(isInside(x,y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x,y,t.dist + 1))

# Driver Code      
if __name__=='__main__':  
    N = 6
    knightpos = [4, 5] 
    targetpos = [1, 1] 
    print(minStepToReachTarget(knightpos, 
                               targetpos, N))                 

#answer = 3




