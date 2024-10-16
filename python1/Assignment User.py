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
            print("User  already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Not enough points to spend.")
            return False
        else:
            self.gold_card_points -= amount
            return True


user1 = User("John", "Doe", "johndoe@example.com", 30)
user1.display_info()

user1_enroll_status = user1.enroll()
print(f"Enroll status: {user1_enroll_status}")

user2 = User("Jane", "Doe", "janedoe@example.com", 25)
user3 = User("Bob", "Smith", "bobsmith@example.com", 40)

user1_spend_status = user1.spend_points(50)
print(f"Spend status: {user1_spend_status}")

user2_enroll_status = user2.enroll()
print(f"Enroll status: {user2_enroll_status}")

user2_spend_status = user2.spend_points(80)
print(f"Spend status: {user2_spend_status}")

user1.display_info()
user2.display_info()
user3.display_info()


user1_reenroll_status = user1.enroll()
print(f"Re-enroll status: {user1_reenroll_status}")

user3_spend_status = user3.spend_points(40)
print(f"Spend status: {user3_spend_status}")