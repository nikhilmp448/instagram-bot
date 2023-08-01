import instaloader
import instaSetup
from colorama import Fore,Style

bot = instaloader.Instaloader()

logger = instaSetup.setup_logging()

user_name = input("enter the username")
profile = instaloader.Profile.from_username(bot.context, user_name)


print(Style.BRIGHT + Fore.BLUE + "---> Username: ", profile.username)
print(Style.BRIGHT + Fore.BLUE + "---> User ID: ", profile.userid)
print(Style.BRIGHT + Fore.BLUE + "---> Number of Posts: ", profile.mediacount)
print(Style.BRIGHT + Fore.BLUE + "---> Followers Count: ", profile.followers)
print(Style.BRIGHT + Fore.BLUE + "---> Following Count: ", profile.followees)
print(Style.BRIGHT + Fore.BLUE + "---> Bio: ", profile.biography)
print(Style.BRIGHT + Fore.BLUE + "---> External URL: ", profile.external_url)

if profile.is_private:
    logger.warning(f"The account '{user_name}' is private. Cannot download posts.")
if profile.mediacount > 0:   
    for post in profile.get_posts():
        bot.download_post(post, target=profile.username)
    logger.info("Download completed successfully.")
else:
    logger.error("zero post to download")