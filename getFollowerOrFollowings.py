import instaloader

def get_followers_and_followings(username):
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()
        
        
        # Login using the credentials
        loader.login("your username", "password")

        # Load the profile of the given username
        profile = instaloader.Profile.from_username(loader.context, username)

        print("1. get followers")
        print("2. get followings")
        user_choice = input("Enter your choice (1 or 2): ")

        # Get all followers
        if user_choice == "1" :
            followers = set(profile.get_followers())
            print(f"Followers of '{username}':")
            for follower in followers:
                print(follower.username)

        # Get all followings
        if user_choice == "2":
            followings = set(profile.get_followees())
            print(f"\nFollowings of '{username}':")
            for following in followings:
                print(following.username)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_followers_and_followings(input("enter the username"))
