def t_or_f() -> bool:

    # open info
    with open("./info.txt", 'r') as file:
        content = file.read()
    #check if websites are already blocked
    if content == "False":
        return False
    else:
        return True


def change():
    # switch the state of true/false of the website blocking
    if blocked == True:
        to_write = False
    else:
        to_write = True
    with open("./info.txt", 'w') as file:
        file.write(str(to_write))


def write():
    with open(hosts, 'r+') as file:
        content = file.read()
        for site in websites:
            for version in site:
                file.write("\n" + redirect + " " + version )
    

def check_pass() -> bool:
    pw = input("Password: ")
    if pw == password:
        return True
    else:
        return False

def for_blocked():
    while True:
        if check_pass():
            with open(hosts, 'w') as file:
                file.write(originalHost)
            print("The websites were unblocked")
            change()
            break
        else:
            print("Wrong password\n")
            continue

def for_not_blocked():
    try:
        write()
        print("The websites were blocked")
        change()
    except:
        print("Sorry! An error ocurred.")


if __name__ == "__main__": 
    # imports
    import os
    from private.password import password
    
    blocked = t_or_f()

    # original host file to restore it
    originalHost = """127.0.0.1	localhost
::1		localhost
127.0.1.1	pop-os.localdomain	pop-os"""
    
    # print on error
    error_str = "Sorry! An error ocurred."

    # host path linux
    hosts = os.path.abspath("/etc/hosts")
    # for testing 
    # hosts = "./hosts_test"

    # redirect to
    redirect = "0.0.0.0"

    # websites to block
    twitch = ["www.twitch.tv", "twitch.tv"]
    reddit = ["www.reddit.com", "reddit.com"]
    discord = ["www.discord.com", "discord.com"]
    facebook = ["www.facebook.com", "facebook.com"]
    messenger = ["www.messenger.com", "messenger.com"]
    instagram = ["www.instagram.com", "instagram.com"]

    websites = [twitch, discord, reddit, facebook, messenger, instagram]

    if blocked:
        for_blocked()
    else:
        for_not_blocked()
        
        
        