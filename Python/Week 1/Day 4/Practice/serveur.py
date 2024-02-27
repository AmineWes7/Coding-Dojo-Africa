class User:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def display_info(self):
        print(f"Name: {self.name}, Points: {self.points}")
        return self
    
    def enroll(self):
        print(f"{self.name} enrolled.")
        return self
    
    def spend_points(self, points):
        self.points -= points
        print(f"{self.name} spent {points} points. Remaining points: {self.points}")
        return self

user1 = User("Amine", 100)
user2 = User("ELWES", 200)

user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()