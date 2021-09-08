def print_numbers(n):
    # prints the numbers from 1 to n in a strainght line
    for i in range(1,n+1):
        print(i,end="")

if __name__ == '__main__':
    n = int(input())
    print_numbers(n)