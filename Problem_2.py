'''
Time Complexity - O(mn) for BFS and DFS.
Space Complexity - O(mn) for both BFS and DFS
Works on Leetcode
'''
from collections import deque
class Solution:
    def __init__(self):
        #create a directions array
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1], [1,-1], [1, 1], [-1,-1], [-1, 1]]
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        m = len(board)
        n = len(board[0])

        #DFS
        # self.dfs(board, m, n, click[0], click[1])
        # return board
        #create a queue

        #BFS
        queue = deque()
        #add click position to queue and mark visited
        queue.append(click)
        board[click[0]][click[1]] = "B"
        while queue:
            #pop neighbor from queue, count mines present
            curr = queue.popleft()
            print(curr)
            r = curr[0]
            c = curr[1]
            cntMines = self.countMines(board, r, c)
            print(cntMines)
            if  cntMines == 0:
                #add neighbors to queue if no mines present, not visited before and mark visited
                for dir in self.dirs:
                    nr = r + dir[0]
                    nc = c + dir[1]
                    if nr >= 0 and nr < m and nc>=0 and nc<n and board[nr][nc] == "E":
                        queue.append([nr,nc])
                        board[nr][nc] = "B"
            else:
                #if mines present then replace the current visited mark by number of mines in neighborhood
                board[r][c] = str(cntMines)
        return board

    def dfs(self, board, m, n, r, c):
        #base condition
        if r < 0 or r == m or c < 0 or c==n or board[r][c] != "E":
            return
        #count mines 
        cntMines = self.countMines(board, r, c)
        #mark visited
        board[r][c] = "B"
        if cntMines == 0:
            #DFS on neighbors if no mines present
            for dir in self.dirs:
                    nr = r + dir[0]
                    nc = c + dir[1]
                    self.dfs(board, m, n, nr, nc)
        else:
            #else replace visited mark by number of mines in neighborhood
            board[r][c] = str(cntMines)

    def countMines(self, board, r, c):
        m = len(board)
        n = len(board[0])
        count = 0
        for dir in self.dirs:
            #check if there is a mine at neighboring position, increment count
            nr = r + dir[0]
            nc = c + dir[1]
            if nr >=0 and nr < m and nc>=0 and nc<n and board[nr][nc] == "M":
                count+=1
        #return total count
        return count

        

        