# good question for learning list comprehension
def list_comprehension(x,y,z,n):
    result = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=n]
    return result
    # newlist = [x for x in fruits if "a" in x]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list_comprehension(x,y,z,n),sep=",")
