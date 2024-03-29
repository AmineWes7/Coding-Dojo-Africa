class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient points to spend.")
            return False
        else:
            self.gold_card_points -= amount
            return True

user1 = User("Amine", "Weslati", "Amine.Weslati@Gmail.com", 19)
user1.display_info()
user1.enroll()
user2 = User("bruce", "wayne", "bruce.wayne@Gmail.com", 35)
user3 = User("Cristiano", "Ronaldo", "Cristiano.Ronaldo@Gmail.com", 39)
user1.spend_points(50)
user2.enroll()
user2.spend_points(80)
user1.display_info()
user2.display_info()