'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0

    if n == 0:
        return 1
    ## check the cache to see if it holds the answer this branch is looking for 
    else:
        return  eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

n = 5

if __name__ == "__main__":
    # Use the main function here to test out your implementation

    print(f"There's {eating_cookies(n)} ways for Cookie Monster to each {n} cookies")
