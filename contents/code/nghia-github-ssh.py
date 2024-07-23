import os
import subprocess
# pip install python-dotenv
from dotenv import load_dotenv

FILE_ENV = "../env/host.env"
FILE_ENV = "../env/localhost.env"
FILE_ENV = "../env/.env"


load_dotenv(FILE_ENV)

SSH_PASSWORD = os.getenv("SSH_PASSWORD")
print(f"🚀SSH_PASSWORD = {SSH_PASSWORD}")
if SSH_PASSWORD == None:
    exit("Create file .env: SSH_PASSWORD")


def create_ssh_config(list_username):
    content = ""
    for username in list_username:
        content += f"""
Host github.com-{username}
    HostName github.com
    User git
    IdentityFile ~/.ssh/{username}
"""

    with open("config", 'w') as file:
    # with open("output/config", 'w') as file:
        file.write(content)


def create_ssh_file(list_username):

    for username in list_username:
        print(f"🚀username = {username}")
        print(f"🚀SSH_PASSWORD = {SSH_PASSWORD}")

        command = [
            "ssh-keygen",
            "-t", "ed25519",
            "-C", f"Account name is: {username}",
            "-f", username,
            "-N", SSH_PASSWORD
        ]
            # "-f", "output/"+username,

        subprocess.run(command, check=True)


def add_ssh_file(list_username):
    try:
        # # Start the SSH agent
        # print("🚀 Starting ssh-agent")
        # subprocess.run("eval $(ssh-agent -s)", shell=True, check=True)

        # Add each SSH key to the SSH agent
        for username in list_username:
            print(f"🚀 Adding SSH key for {username}")
            ssh_key_path = f"{username}"

            try:
                # Add the SSH key to the ssh-agent
                #     # auto SSH_PASSWORD  subprocess.run(["ssh-add"
                # Enter passphrase for  :
                subprocess.run(["ssh-add", ssh_key_path], check=True)
                print(f"Successfully added SSH key for {username}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to add SSH key for {username}: {e}")

    except subprocess.CalledProcessError as e:
        print(f"Failed to start ssh-agent: {e}")


def create_symlink(list_username):
    list_file = []

    list_file.append("config")

    for username in list_username:
        list_file.append(f"{username}")
        list_file.append(f"{username}.pub")

    for path in list_file:
        symlink_path = os.path.expanduser(f"~/.ssh/{path}")

        if os.path.exists(symlink_path):
            print(f"The symbolic link already exists: {path}")
        else:
            try:
                os.symlink(os.path.abspath(path), symlink_path)
                print(f"Symbolic link created at: {symlink_path}")
            except OSError as e:
                print(f"Failed to create symbolic link: {e}")


if __name__ == "__main__":

    list_username = [
        "whynotnghiavu",
        "company20206205",
        "20206205",

        "vvn20206205",
        "hust20206205",
        "vuvannghia452002",
    ]


    print(f"👉 Step: create_ssh_config")
    create_ssh_config(list_username)

    print(f"👉 Step: create_ssh_file")
    create_ssh_file(list_username)

    print(f"👉 Step: create_symlink")
    create_symlink(list_username)

    print(f"👉 Step: add_ssh_file")
    add_ssh_file(list_username)
