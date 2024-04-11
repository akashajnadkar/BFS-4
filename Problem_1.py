'''
Time Complexity - O(6n^2). N^2 positions with each having 6 possibilities
Space Complexity - O(n^2). We are using an array for the flattened board

Works on Leetcode
'''
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        arr = [0] * (m*n)
        flag = False
        idx = 0
        r, c = m-1, 0
        while idx < len(arr):
        #flatten a matrix to an array
            if board[r][c] == -1:
                arr[idx] = -1
            else:
                arr[idx] = board[r][c] - 1
            idx+=1
            if not flag:
                c+=1
                if c == n:
                    c-=1
                    r-=1
                    flag = True
            else:
                c-=1
                if c<0:
                    c+=1
                    r-=1
                    flag = False
        #create a queue and add the first position to queue and mark it visited
        queue = deque()
        queue.append(0)
        arr[0] = -2
        moves=0
        while queue:
            # 1 move can be a roll of ice between 1 and 6 
            size = len(queue)
            #maintain a size to divide between moves
            for  i in range(size):
                #process a position, check if its final position
                curr = queue.popleft()
                print(curr)
                if curr == len(arr) -1:
                    #return the total moves if position is final position
                    return moves
                for j in range(1,7):
                    #add to queue next 6 positions from the current board and mark visited
                    #if the position has ladder or snake add the destination to queue as well
                    if curr + j < len(arr):
                        newPos = curr + j
                        if arr[newPos] != -2:
                            if arr[newPos] == -1:
                                queue.append(newPos)
                                arr[newPos] = -2
                            else:
                                queue.append(arr[newPos])
                                arr[newPos] = -2
            moves+=1
        return -1
        