def countDigitOne(n):
    countr = 0
    for i in range(1, n + 1):
        str_i = str(i)
        countr += str_i.count('1')
    return countr

if __name__ == "__main__":
    n = int(input())
    print(countDigitOne(n))
    
