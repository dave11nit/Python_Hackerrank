# Find the Runner up score
# finding the score of runner up from a given list
def runner_up(n, arr):
    # create a set out of list
    # again create a list out of it
    # this will eliminate the repeated elements
    # then sort the list
    # and take the second element
    print(sorted(list(set(arr)))[-2])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(n, arr)