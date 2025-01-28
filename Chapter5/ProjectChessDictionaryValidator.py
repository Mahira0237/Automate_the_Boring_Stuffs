import sys
board={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
def isValidChessBoard(board):
    letters=['a','b','c','d','e','f','g','h']
    BK,WK,B,W,BP,WP=0,0,0,0,0,0
    k=list(board.keys())
    v=list(board.values())
    for i in k:
        if (int(i[0])>8) or (i[1] not in letters):
            print('The Chessboard is invalid')
            sys.exit()
    for j in v:
        if j[0]=='b':
            B+=1
        elif j[0]=='w':
            W+=1
        if j=='bking':
            BK+=1
        elif j=='wking':
            WK+=1
        if j=='bpawn':
            BP+=1
        elif j=='wpawn':
            WP+=1
    if (BK!=1) or (WK!=1) or (W>16) or (B>16) or (BP>8) or (WP>8):
        print('The Chessboard is invalid')
    else: print('The Chessboard is valid')       

isValidChessBoard(board)