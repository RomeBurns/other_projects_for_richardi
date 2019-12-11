import random
class cards:
    def many(self):
        val = int(input("How many cards do you want to guess from? "))
        self.val = val

    def monty(self):
        self.rand = random.randint(1, self.val)

    def cards(self):
        for i in range(self.val):
            print("##  ", end = "")
        print("")
        for i in range(self.val):
            print("##  ", end = "")
        print("")
        for i in range(self.val):
            print(i + 1, end = "   ")

    def guess(self):
        self.g = int(input("Which one is the ace? The rest are all jacks. "))
        if self.g == self.rand:
            print("correct!")
        else:
            print("incorrect!")

    def showcards(self):
        for i in range(self.val):
            if i != self.rand:
                print("JJ  ", end = "")
            else:
                print("AA  ", end = "")
        print("")
        for i in range(self.val):
            if i != self.rand:
                print("JJ  ", end = "")
            else:
                print("AA  ", end = "")

deck = cards()
deck.many()
deck.monty()
deck.cards()
deck.guess()
deck.showcards()