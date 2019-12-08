import numpy as np

def mp3(e):
    x = e[:,0]
    y = e[:,1]
    for n in range(len(e)):
        a = np.polyfit(x, y, n)
        b = np.polyval(a, x)    
        c = np.linalg.norm(y - b)    
        d = [n,c]
        
        if n == 0:        
            m = d
            
        elif m[1] >= d[1]:        
            z = d[0]
            
    p = np.polyfit(x, y, z)
    
    print('The coefficients are: ',p)

e1 = input("Input experimental points: ")
mp3(eval(e1))

# The e is the experimental points. 
# The input should be in a nx2 matrix, for example: experimental points = np.array([[1,1],[2,2]]).
    