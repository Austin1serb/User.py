class User:
    def __init__(self, first_name, last_name, email, age,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Name: {self.is_rewards_member}")
        print(f"Name: {self.gold_card_points}")

    def enroll(self):
        self.is_rewards_member = True
        print(f'{self.first_name} {self.last_name} is a rewards member')
    
    def spend_points(self, amount):
        if self.is_rewards_member:
            self.gold_card_points += amount
            print(f"{self.first_name} {self.last_name} has {amount} points")
        else:
            print("The User is not a gold card rewards member")

user1 = User("austin", "Serb", "john@gmail", 30,)
user1.display_info()
user1.enroll()
user1.spend_points(50)


user2 = User("eddy", "Serb", "eddy@gmail", 23,)
user2.display_info()
user2.enroll()
user2.spend_points(80)

user3 = User("christine", "Serb", "krissy@gmail", 32,)
user3.display_info()

