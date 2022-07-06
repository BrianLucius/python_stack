class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"\nFirst name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"is_rewards_member: {self.is_rewards_member}")
        print(f"gold_card_points: {self.gold_card_points}")
    
    def enroll(self):
        if self.is_rewards_member:
            print(f"\n{self.first_name} is already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return True
    
    def spend_points(self, points):
        if not self.gold_card_points >= points:
            difference = points - self.gold_card_points
            print(f"\n{self.first_name}, you do not have enough points to redeem.")
            print(f"You need to earn {difference} more points.")
            return
        self.gold_card_points -= points
        print(f"\n{self.first_name}, you have redeemed {points} points.")
        print(f"Your new points balance is {self.gold_card_points}")
        return
        

user_brian = User("Brian", "Lucius", "brian@brianlucius.net", "42")
user_brian.display_info()

user_kenza = User("Kenza", "Funk", "kenza@email.com", "43")
user_kenza.display_info()

user_zira = User("Zira", "Funk", "zira@email.com", "16")
user_zira.display_info()

enroll_status = user_brian.enroll()
print(f"\n{user_brian.first_name} enrolled: {enroll_status}")
user_brian.spend_points(50)

print(f"\n{user_kenza.first_name} enrolled: {user_kenza.enroll()}")
user_kenza.spend_points(80)

user_brian.display_info()
user_kenza.display_info()
user_zira.display_info()

user_brian.enroll()
user_zira.spend_points(40)