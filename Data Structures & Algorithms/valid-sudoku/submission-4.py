class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        break the board into 3x3 boxes (each one going into a 1d array)
        iterate through each array
        hashmap to see if there's duplicates (except for empty squares)
        return true
        """
        rows = []
        subBoards = [
            [],[],[],[],[],[],[],[],[]
        ]

        rowExtantValues = [
            [],[],[],[],[],[],[],[],[]
        ] # row 0: [1,2,3]
        columnExtantValues = [
            [],[],[],[],[],[],[],[],[]
        ] # row 0: [1,2,3]
        for y in range(len(board)):
            column = board[y]
            
            for x in range(len(column)):
                value = board[x][y]
                if value == ".": continue
                # sub 1: x = 0-2, y = 0-2
                # sub 2: x = 3-5, y = 0-2
                # sub 3: x = 6-8, y = 0-2
                # sub 4: x = 0-2, y = 3-5
                # sub 5: x = 3-5, y = 3-5
                # sub 6: x = 6-8, y = 3-5
                # sub 7: x = 0-2, y = 6-8
                # sub 8: x = 3-5, y = 6-8
                # sub 9: x = 6-8, y = 6-8

                if value in columnExtantValues[x]: return False
                columnExtantValues[x].append(value)

                if value in rowExtantValues[y]: return False
                rowExtantValues[y].append(value)

                subBoardIndex = 0
                if y < 3: subBoardIndex += 0
                elif y < 6: subBoardIndex += 3
                else: subBoardIndex += 6

                if x < 3: subBoardIndex += 0
                elif x < 6: subBoardIndex += 1
                else: subBoardIndex += 2

                subBoards[subBoardIndex].append(value)
        
        for subBoard in subBoards:
            extantValues = set()
            for value in subBoard:
                if value in extantValues: return False
                extantValues.add(value)
        
        return True