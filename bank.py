class bankaccount():
    def __init__(self,d,w,s):
        self.d=d
        self.w=w
        self.s=s
    def deposit(self):
        self.s=self.s+self.d
    def withdraw(self):
        self.s=self.s-self.w
x=input("how much u want to deposit")
y=input("type the withdraw")
z=1234
bankaccount(x,y,z)