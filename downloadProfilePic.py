import instaloader

def download_profile_picture(username):
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()

        # Load the profile of the given username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download the profile picture
        loader.download_profile(profile, profile_pic_only=True)

        print(f"Profile picture downloaded successfully for '{username}'.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace 'your_username' with the Instagram username you want to download the profile picture from
    download_profile_picture(input("enter the username : "))
