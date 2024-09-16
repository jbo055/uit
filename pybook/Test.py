class Apple:
    def __init__(self, weight = 1):
        self.weight = weight
        print("Apple constructor")

    def __str__(self):
        return "Apple: " + str(self.weight)
    
class GoldenDelicious(Apple):
    def __init__(self, weight = 5):
        super().__init__(weight) 
        print("GoldenDelicious non-arg constructor")

    def __str__(self):
        return "GoldenDelicious: " + str(self.weight)

def main():
    a = Apple()
    print(a)
    print("---------------")
    
    g = GoldenDelicious(7)
    print(g)
    print("---------------")

    c = GoldenDelicious(8)
    print(c)

main()