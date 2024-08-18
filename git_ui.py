# Copyright (c) 2009-2022 Volodymyr Frytskyy (https://www.vladonai.com/about-resume)
#
# This script is a simplification tool for daily Git routines. It is a generic script that can be useful for working with GitHub, and it is easy to configure.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import subprocess
import json
from colorama import Fore, Style

CONFIG_FILE = "git_ui_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        return {
            "remote_name": "origin",
            "main_branch": "main", 
            "personal_branch": "vlad"
        }

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def get_current_branch():
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()

def print_current_config(config, b_show_ext_remote_config=False):
    current_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
    print(f"{Fore.GREEN}Remote repository:{Style.RESET_ALL} {config['remote_name']}, {Fore.GREEN}Remote Main branch:{Style.RESET_ALL} {config['main_branch']}, {Fore.GREEN}Remote Personal branch:{Style.RESET_ALL} {config['personal_branch']}")
    print(f"{Fore.GREEN}Current Local Branch:{Style.RESET_ALL} {current_branch}")
    if b_show_ext_remote_config:
        print(f"{Fore.GREEN}Global User Name:{Style.RESET_ALL} {subprocess.check_output(['git', 'config', '--global', 'user.name'], text=True).strip()}")
        print(f"{Fore.GREEN}Global User Email:{Style.RESET_ALL} {subprocess.check_output(['git', 'config', '--global', 'user.email'], text=True).strip()}")
        print(f"{Fore.GREEN}Remote repositories avilable:{Style.RESET_ALL}")
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")

def show_checkout_menu(config):
    print_current_config(config)
    print("Select a checkout option:")
    print("[1] Checkout/get changes from remote repository")
    print("[2] Show changes on remote repository")
    print("[3] List branches")
    print("[4] Create new branch")
    print("[5] Switch to a specific branch")
    print("[6] Checkout a specific commit")
    print("[7] Checkout a specific tag")
    print("[8] Sync/merge changes from main branch to local branch")
    print("[0] Back to main menu")
    
def handle_checkout_option(option, config):
    if option == "1":
        os.system(f"git pull {config['remote_name']} {config['personal_branch']}")
    elif option == "2":
        os.system("git fetch")
    elif option == "3":
        os.system("git branch -a")
    elif option == "4":
        branch_name = input("Enter new branch name: ")
        os.system(f"git checkout -b {branch_name}")
    elif option == "5":
        branch_name = input("Enter branch name to switch to: ")
        os.system(f"git checkout {branch_name}")
    elif option == "6":
        commit_hash = input("Enter commit hash to checkout: ")
        os.system(f"git checkout {commit_hash}")
    elif option == "7":
        tag_name = input("Enter tag name to checkout: ")
        os.system(f"git checkout {tag_name}")
    elif option == "8":
        sync_changes_from_main_branch(config)
    elif option == "0":
        return
    else:
        print("Invalid option.")

def sync_changes_from_main_branch(config):
    os.system(f"git checkout {config['personal_branch']}")  # Switch to personal branch
    os.system(f"git pull {config['remote_name']} {config['main_branch']}")  # get latest changes from main branch on remote repository
    os.system(f"git merge {config['main_branch']}")  # get latest changes from main branch on remote repository
    os.system(f"git push")  # push merge result in personal branch to remote repository
    print(f"Changes from {config['main_branch']} branch have been synchronized to {config['personal_branch']} branch.")
    
def show_commit_push_menu(config):
    print_current_config(config)
    print("Select a commit message:")
    print("[1] Daily snapshot of work in progress")
    print("[2] Bug fixes")
    print("[3] Refactored and cleaned up the code")
    print("[4] Optimized performance and efficiency")
    print("[5] Documentation update")
    print("[6] Merge changes from another branch")
    print("[7] Security improvements")
    print("[8] Dependency updates")
    print("[9] Configuration changes")
    print("[10] Amend the last commit [modify last commit]")
    print("[11] Stash changes [temporarily hide changes]")
    print("[12] Apply stashed changes [apply hidden changes]")
    print("[0] Other (specify)")

def handle_commit_push_option(option, config):
    commit_messages = {
        "1": "Daily snapshot of work in progress",
        "2": "Bug fixes",
        "3": "Refactored and cleaned up the code",
        "4": "Optimized performance and efficiency",
        "5": "Documentation update",
        "6": "Merge changes from another branch",
        "7": "Security improvements",
        "8": "Dependency updates",
        "9": "Configuration changes",
    }

    if option == "0":
        commit_message = input("Enter commit message: ")
    elif option == "10":
        os.system("git commit --amend")
        return
    elif option == "11":
        os.system("git stash")
        return
    elif option == "12":
        os.system("git stash apply")
        return
    else:
        commit_message = commit_messages.get(option, "")

    os.system("git add -u")
    diff_result = subprocess.run(["git", "diff", "--cached", "--exit-code"], capture_output=True)

    if diff_result.returncode != 0:
        os.system(f'git commit -m "{commit_message}"')
        os.system(f"git push -u {config['remote_name']} {config['personal_branch']}")
    else:
        print("No changes to commit.")

def show_local_repo_menu(config):
    print_current_config(config)
    print("Select a local repository option:")
    print("[1] Show local changes")
    print("[2] Find who introduced text change")
    print("[3] Show commit history")
    print("[4] Show status")
    print("[5] Show file history")
    print("[6] Show branch history")
    print("[7] Reset to a specific commit")
    print("[8] Revert a specific commit")
    print("[0] Back to main menu")

def handle_local_repo_option(option):
    if option == "1":
        os.system("git diff")
    elif option == "2":
        text_change = input("Enter the text change to search for: ")
        os.system(f"git log -S'{text_change}'")
    elif option == "3":
        os.system("git log")
    elif option == "4":
        os.system("git status")
    elif option == "5":
        file_name = input("Enter the file name: ")
        os.system(f"git log -p {file_name}")
    elif option == "6":
        branch_name = input("Enter the branch name: ")
        os.system(f"git log {branch_name}")
    elif option == "7":
        commit_hash = input("Enter the commit hash to reset to: ")
        os.system(f"git reset --hard {commit_hash}")
    elif option == "8":
        commit_hash = input("Enter the commit hash to revert: ")
        os.system(f"git revert {commit_hash}")
    elif option == "0":
        return
    else:
        print("Invalid option.")

def show_branch_menu(config):
    print_current_config(config)
    print("Select a branch option:")
    print("[1] List branches")
    print("[2] Create a new branch")
    print("[3] Delete a branch")
    print("[4] Merge branches")
    print("[5] Rebase branches")
    print("[6] Push new branch to remote")
    print("[0] Back to main menu")

def handle_branch_option(option, config):
    if option == "1":
        os.system("git branch -a")
    elif option == "2":
        branch_name = input("Enter new branch name: ")
        os.system(f"git checkout -b {branch_name}")
    elif option == "3":
        branch_name = input("Enter branch name to delete: ")
        os.system(f"git branch -d {branch_name}")
    elif option == "4":
        branch_name = input("Enter branch name to merge: ")
        os.system(f"git merge {branch_name}")
    elif option == "5":
        branch_name = input("Enter branch name to rebase: ")
        os.system(f"git rebase {branch_name}")
    elif option == "6":
        branch_name = input("Enter branch name to push to remote: ")
        remote_name = input("Enter remote name (e.g., origin, repo1): ")
        os.system(f"git push -u {remote_name} {branch_name}")  # Пуш нової гілки на віддалений сервер
    elif option == "0":
        return
    else:
        print("Invalid option.")

def show_tag_menu(config):
    print_current_config(config)
    print("Select a tag option:")
    print("[1] List tags")
    print("[2] Create a new tag")
    print("[3] Delete a tag")
    print("[0] Back to main menu")

def handle_tag_option(option):
    if option == "1":
        os.system("git tag")
    elif option == "2":
        tag_name = input("Enter new tag name: ")
        os.system(f"git tag {tag_name}")
    elif option == "3":
        tag_name = input("Enter tag name to delete: ")
        os.system(f"git tag -d {tag_name}")
    elif option == "0":
        return
    else:
        print("Invalid option.")

def show_configure_menu(config):
    print_current_config(config, True)
    print("Select a configuration option:")
    print("[1] Set main branch name")
    print("[2] Set personal branch name")
    print("[3] Add remote repository [+ clone]")
    print("[4] Remove remote repository")
    print("[5] Switch to remote repository")
    print("[6] Set global user name")
    print("[7] Set global user email")
    print("[0] Back to main menu")

def handle_configure_option(option, config):
    if option == "1":
        main_branch = input("Enter main branch name: ")
        config["main_branch"] = main_branch
    elif option == "2":
        personal_branch = input("Enter personal branch name: ")
        config["personal_branch"] = personal_branch
    elif option == "3":
        name = input("Enter remote repository name: ")
        url = input("Enter remote repository URL: ")
        result = subprocess.run(["git", "remote", "add", name, url], capture_output=True, text=True)
        if result.returncode == 0:
            directory = input("Enter local directory to clone repository to: ")
            result = subprocess.run(["git", "clone", url, directory], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error: {result.stderr}")
        else:
            print(f"Error: {result.stderr}")
    elif option == "4":
        name = input("Enter remote repository name to remove: ")
        result = subprocess.run(["git", "remote", "remove", name], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
    elif option == "5":
        name = input("Enter remote repository name to switch to: ")
        result = subprocess.run(["git", "remote", "set-url", "origin", name], capture_output=True, text=True)
        if result.returncode == 0:
            config["remote_name"] = name
        else:
            print(f"Error: {result.stderr}")
    elif option == "6":
        name = input("Enter global user name: ")
        result = subprocess.run(["git", "config", "--global", "user.name", name], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
    elif option == "7":
        email = input("Enter global user email: ")
        result = subprocess.run(["git", "config", "--global", "user.email", email], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
    elif option == "0":
        return
    else:
        print("Invalid option.")
    save_config(config)

def show_main_menu(config):
    print_current_config(config)
    print("Select an option:")
    print("[1] Checkout")
    print("[2] Commit/Push")
    print("[3] Local repository")
    print("[4] Branch")
    print("[5] Tag")
    print("[9] Configure")
    print("[0] Exit")

def main():
    config = load_config()

    while True:
        show_main_menu(config)
        main_option = input("Enter your choice (1-5, 0): ")

        if main_option == "1":
            while True:
                show_checkout_menu(config)
                checkout_option = input("Enter your choice (1-7, 0): ")
                handle_checkout_option(checkout_option, config)
                if checkout_option == "0":
                    break
        elif main_option == "2":
            show_commit_push_menu(config)
            commit_push_option = input("Enter your choice (1-12, 0): ")
            handle_commit_push_option(commit_push_option, config)
        elif main_option == "3":
            while True:
                show_local_repo_menu(config)
                local_repo_option = input("Enter your choice (1-8, 0): ")
                handle_local_repo_option(local_repo_option)
                if local_repo_option == "0":
                    break
        elif main_option == "4":
            while True:
                show_branch_menu(config)
                branch_option = input("Enter your choice (1-5, 0): ")
                handle_branch_option(branch_option, config)
                if branch_option == "0":
                    break
        elif main_option == "5":
            while True:
                show_tag_menu(config)
                tag_option = input("Enter your choice (1-3, 0): ")
                handle_tag_option(tag_option)
                if tag_option == "0":
                    break
        elif main_option == "9":
            while True:
                show_configure_menu(config)
                configure_option = input("Enter your choice (1-3, 0): ")
                handle_configure_option(configure_option, config)
                if configure_option == "0":
                    break
        elif main_option == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
