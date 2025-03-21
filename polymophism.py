print("Welcome to Polymorphism Challenge: \n")

#define the function

def polymorphism_challenge():
    class Animals:
        def __init__(self,name):
            self.name=name
        def move(self):
            return "Animals have different movement Methods"
    class Snakes(Animals):
        def move(self):
            return "Serpentine"
    snake=Snakes("Cobra")
    print("snake name:",snake.name)
    print("movement:",snake.move(),"\n")

    class Dogs(Animals):
        def move(self):
            return "Running"
    dog=Dogs("Cocker Spaniel")
    print("Dog name:",dog.name)
    print("movement:",dog.move())

#call thefunction to execute the codes
polymorphism_challenge()