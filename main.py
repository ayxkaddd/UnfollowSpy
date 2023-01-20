import os
from instagrapi import Client


class Inst_Tools:

    folder = "files"
    file_name="current_followers.txt"

    app = Client()

    def __init__(self, username, password, ig_account_id):
        self.username = username
        self.password = password
        self.ig_account_id = ig_account_id


    def get_followers(self):

        os.system(f"copy {path}/{Inst_Tools.file_name} {path}/backup_followers.txt")
        os.system(f"copy {path}/{Inst_Tools.file_name} {path}/old_followers.txt")
        os.system(f"del /Q {path}/{Inst_Tools.file_name}")
    
        Inst_Tools.app.login(self.username, self.password)
        usernames = Inst_Tools.app.user_followers(self.ig_account_id)
        
        file = open(f"{path}/{Inst_Tools.file_name}", "a")

        for i in usernames:
            a = str(usernames[i])
            # cancer
            stage_1 = a.split("full_name='")[0]
            stage_2 = stage_1.split("username='")[1].split("',")[0]
            stage_3 = stage_2.split("'")[0]
            file.write(f"{stage_3}\n")

        file.close()

        old = open(f"{path}/old_followers.txt").readlines()
        new = open(f"{path}/{Inst_Tools.file_name}").readlines()
        old_2 = []
        new_2 = []

        for i in old:
            old_2.append(i.split("\n")[0])        
        for i in new:
            new_2.append(i.split("\n")[0])

        temp3 = []

        for follower in old_2:
            if follower not in new_2:
                temp3.append(follower)

        return temp3


    def total_followers(self):
        file = open(f"{path}/{Inst_Tools.file_name}", "r")
        c = len(file.readlines())
        return c


    def check_if_follow(self, query):
        file = open(f"{path}/{Inst_Tools.file_name}", "r")
        
        for i in file.readlines():
            if query == i.split("\n")[0]:
                return True
        
        return False