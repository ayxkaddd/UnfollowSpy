from colorama import init, Fore

init(autoreset=True)

import config
from main import Inst_Tools

ig_id = config.ig_account_id
username=f"{config.ig_username}"
password=f"{config.ig_password}"

app = Inst_Tools(username, password, ig_id)


def total_followers():
    total_followers = app.total_followers()
    print(f"you have - {Fore.RED}{total_followers}")


def check_if_follow(username):
    if app.check_if_follow(username):
        print(f"{Fore.GREEN}{username} following you")
    else:
        print(f"{Fore.RED}nah")


def check_if_unfollow():
    unfollow_list = app.get_followers()
    if unfollow_list:
        for i in unfollow_list:
            print(f"\n{Fore.RED}https://www.instagram.com/{i}/")
    else:
        print(f"\n{Fore.GREEN}no one has unfollow")


def main():
    help = """
[1] total_followers - returns you a number of your followers
[2] check_if_follow [username] - return True if user have following you
[3] check_if_unfollow - goes through all your followers and check if any one has unfollowed you
"""
    print(help)
    user_query = input("which command do u wanna use?\n> ")
    if user_query == "1":
        total_followers()
    elif user_query == "2":
        check_if_follow(user_query.split(" ")[-1])
    elif user_query == "3":
        check_if_unfollow()


if __name__ == "__main__":
    main()