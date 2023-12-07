# to return the length of the last word in the string
def main():
    n = input()  
    
    count = 0
    i = len(n) - 1
    
    while i >= 0:
        if n[i] != ' ':
            count += 1
        else:
            break
        i -= 1
    
    print(count)

if __name__ == "__main__":
    main()
