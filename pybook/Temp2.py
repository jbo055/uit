class A:
    def __str__(self):
        return "A"

class B(A):
    pass

class C(B):
    pass
    
def main():
    b = B()
    a = A()
    c = C()
    print(a, b, c)

main()