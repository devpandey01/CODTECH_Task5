class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = {"friends": [], "messages": []}
            print(f"User '{username}' registered successfully.")
        else:
            print(f"User '{username}' already exists.")

    def add_friend(self, username, friend_username):
        if username in self.users and friend_username in self.users:
            if friend_username not in self.users[username]["friends"]:
                self.users[username]["friends"].append(friend_username)
                print(f"User '{friend_username}' added as a friend to '{username}'.")
            else:
                print(f"User '{friend_username}' is already a friend of '{username}'.")
        else:
            print("Both users must be registered to add friends.")

    def send_message(self, username, friend_username, message):
        if username in self.users and friend_username in self.users[username]["friends"]:
            self.users[username]["messages"].append({"to": friend_username, "message": message})
            print(f"Message sent to {friend_username}.")
        else:
            print(f"{friend_username} is not a friend of {username} or users do not exist.")

    def display_users(self):
        print("Registered users:")
        for user in self.users:
            print(user)

    def display_friends(self, username):
        if username in self.users:
            friends = self.users[username]["friends"]
            if friends:
                print(f"{username}'s friends: {', '.join(friends)}")
            else:
                print(f"{username} has no friends added yet.")
        else:
            print(f"User '{username}' does not exist.")

    def display_messages(self, username):
        if username in self.users:
            messages = self.users[username]["messages"]
            if messages:
                print(f"Messages sent by {username}:")
                for message in messages:
                    print(f"To {message['to']}: {message['message']}")
            else:
                print(f"{username} has not sent any messages.")
        else:
            print(f"User '{username}' does not exist.")

def menu():
    platform = SocialMediaPlatform()

    while True:
        print("\n--- Social Media Platform ---")
        print("1. Register User")
        print("2. Add Friend")
        print("3. Send Message")
        print("4. Display Users")
        print("5. Display Friends")
        print("6. Display Messages")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter the username to register: ")
            platform.register_user(username)

        elif choice == '2':
            username = input("Enter your username: ")
            friend_username = input("Enter the friend's username to add: ")
            platform.add_friend(username, friend_username)

        elif choice == '3':
            username = input("Enter your username: ")
            friend_username = input("Enter the friend's username to send a message: ")
            message = input("Enter your message: ")
            platform.send_message(username, friend_username, message)

        elif choice == '4':
            platform.display_users()

        elif choice == '5':
            username = input("Enter your username: ")
            platform.display_friends(username)

        elif choice == '6':
            username = input("Enter your username: ")
            platform.display_messages(username)

        elif choice == '7':
            break

        else:
            print("Invalid choice! Please try again.")

menu()
