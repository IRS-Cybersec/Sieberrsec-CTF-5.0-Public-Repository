import random

def init():
    global flag, juryAns
    with open('flag.txt', 'r') as handler: # read flag
        flag = handler.read()
    juryAns = [random.getrandbits(32) for _ in range(0, 625)]

def ansQuery():
    st = int(input()) - 1 # input start of range of XOR query, 1-indexed
    en = int(input()) - 1 # input end of range of XOR query, 1-indexed
    assert(0 <= st <= 624 and 0 <= en <= 624) # check for no out-of-bounds list reference
    ans = 0
    for pos in range(st, en + 1): # python ranges are end-exclusive so + 1
        ans ^= juryAns[pos]
    print(ans)

def main():
    init()
    print("Guess my list of numbers of length 625 and get a flag!")
    print("\nYou have 624 queries, for each query, enter the start and end of some range")
    print("I will respond with the XOR of the entire range")
    print("NOTE: Queries are all 1-indexed and inclusive of start/end")
    print("\nAt the end, if you can guess my array I will give you a flag!")
    print("Your queries start now, good luck!")
    for i in range(0, 624):
        ansQuery()
    print("\nNow, enter your array guess with each value in the array separated by a space")
    playerAns = list(map(int, input().split(' ')))
    if playerAns == juryAns:
        print(f"\nYou got it! Here is your flag: {flag}")
    else:
        print("Wrong answer, better luck next time :(")

if __name__ == "__main__":
    main()