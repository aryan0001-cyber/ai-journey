
def main():
    x=input("type a word :  ")
    palindrome(x)
def palindrome(n):
        l = len(n)   
        if n[0]==n[l-1]:
              print("its a palindrome")
        else:
              print("not a palindrome")
main()
