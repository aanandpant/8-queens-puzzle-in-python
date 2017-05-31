import json

def isattack(board,r,c):
    for i in range(r):
        if(board[i][c]==1):
            return True
    
    i=r-1
    j=c-1
    while((i>=0) and (j>=0)):
        if(board[i][j]==1):
            return True
        i=i-1
        j=j-1
    
    i=r-1
    j=c+1
    while((i>=0) and (j<8)):
        if(board[i][j]==1):
            return True
        i=i-1
        j=j+1
    return False
    
def solve(board,row):
    i=0
    while(i<8):
        if(not isattack(board, row, i)):
            board[row][i]=1
            if(row==7):
                return True
            else:
                if(solve(board, row+1)):
                    return True
                else:
                    board[row][i]=0
        i=i+1
    
    if(i==8):
        return False
    
def printboard(board):
    for i in range(8):
        for j in range(8):
            print str(board[i][j])+"  ",
        print "\n"
        
board = [[0 for x in range(8)] for x in range(8)]

if __name__ == '__main__':
    data=[]
    with open('ip.json') as f:
        data=json.load(f)
    
    if(data["start"]<0 or data["start"]>7):
        print "Invalid JSON input"
        exit()
    
    board[0][data["start"]]=1
    if(solve(board, 1)):
        print "Queens problem solved!!!"
        print "Board Configuration:"
        printboard(board)
    else:
        print "Queens problem not solved!!!"

"""
ip.json
{"start":5}
"""


"""
----output----
scavenger@ubuntu16:~$ ssh pi@192.168.1.6
pi@192.168.1.6's password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Apr  2 14:17:09 2017

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@raspberrypi:~ $ python queen.py
Queens problem solved!!!
Board Configuration:
0   0   0   0   0   1   0   0   

1   0   0   0   0   0   0   0   

0   0   0   0   1   0   0   0   

0   1   0   0   0   0   0   0   

0   0   0   0   0   0   0   1   

0   0   1   0   0   0   0   0   

0   0   0   0   0   0   1   0   

0   0   0   1   0   0   0   0  
"""
