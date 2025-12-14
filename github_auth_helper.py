#!/usr/bin/env python
"""
GitHub Authentication Helper for Banking Bot
Provides guidance and automates authentication setup
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, cwd=None):
    """Run a shell command"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)


def setup_github_auth():
    """Help set up GitHub authentication"""
    print("=" * 70)
    print("GitHub Authentication Setup")
    print("=" * 70)
    print()
    
    repo_path = r"C:\Users\rajni\Tourism_Bot\banking_bot"
    
    print("Choose your authentication method:\n")
    print("1) GitHub CLI (Recommended - easiest)")
    print("2) Personal Access Token (PAT)")
    print("3) SSH Keys")
    print("4) Exit")
    print()
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        setup_github_cli(repo_path)
    elif choice == "2":
        setup_pat(repo_path)
    elif choice == "3":
        setup_ssh(repo_path)
    else:
        print("Exiting...")
        return


def setup_github_cli(repo_path):
    """Setup using GitHub CLI"""
    print("\n" + "=" * 70)
    print("GitHub CLI Setup")
    print("=" * 70)
    
    print("\n1. Install GitHub CLI from: https://cli.github.com/")
    print("   Or if using Winget: winget install GitHub.cli")
    print("\n2. After installation, open PowerShell and run:")
    print("   gh auth login")
    print("\n3. Follow the prompts:")
    print("   - Choose 'GitHub.com'")
    print("   - Choose 'HTTPS'")
    print("   - Choose 'Y' for authenticating with git")
    print("   - Choose 'Y' for creating personal access token")
    print("\n4. After authentication, push with:")
    print("   cd c:\\Users\\rajni\\Tourism_Bot\\banking_bot")
    print("   git push -u origin master")
    
    input("\nPress Enter when you've completed GitHub CLI setup...")
    
    code, out, err = run_command(
        f'"{r"C:\Program Files\Git\cmd\git.exe"}" push -u origin master',
        cwd=repo_path
    )
    
    if code == 0:
        print("\n✓ Successfully pushed to GitHub!")
    else:
        print(f"\nPush output: {out}")
        if err:
            print(f"Error: {err}")


def setup_pat(repo_path):
    """Setup using Personal Access Token"""
    print("\n" + "=" * 70)
    print("Personal Access Token (PAT) Setup")
    print("=" * 70)
    
    print("\n1. Go to: https://github.com/settings/tokens")
    print("\n2. Click 'Generate new token' -> 'Generate new token (classic)'")
    print("\n3. Settings:")
    print("   - Note: Banking Bot")
    print("   - Expiration: 30 days (or as needed)")
    print("   - Scopes: Check 'repo' (full control of private repositories)")
    print("\n4. Click 'Generate token' and copy it")
    print("\n5. Return here and paste the token")
    
    pat = input("\nPaste your Personal Access Token: ").strip()
    
    if not pat:
        print("✗ No token provided")
        return
    
    # Configure git with PAT
    git_exe = r'C:\Program Files\Git\cmd\git.exe'
    
    # Update remote URL with PAT
    url_with_pat = f"https://{pat}@github.com/rajnishchp/Bankingbot.git"
    
    print("\nConfiguring git with token...")
    code, out, err = run_command(
        f'"{git_exe}" remote set-url origin "{url_with_pat}"',
        cwd=repo_path
    )
    
    print("Pushing to GitHub...")
    code, out, err = run_command(
        f'"{git_exe}" push -u origin master',
        cwd=repo_path
    )
    
    if code == 0:
        print("\n✓ Successfully pushed to GitHub!")
        print("\nNote: To keep your token safe, run:")
        print(f'  git remote set-url origin "https://github.com/rajnishchp/Bankingbot.git"')
    else:
        print(f"\nPush output: {out}")
        if err:
            print(f"Error: {err}")


def setup_ssh(repo_path):
    """Setup using SSH keys"""
    print("\n" + "=" * 70)
    print("SSH Key Setup")
    print("=" * 70)
    
    print("\n1. Generate SSH key (if you don't have one):")
    print('   ssh-keygen -t ed25519 -C "rajnishchp@gmail.com"')
    
    print("\n2. Add SSH key to SSH agent:")
    print("   eval $(ssh-agent -s)")
    print('   ssh-add ~/.ssh/id_ed25519')
    
    print("\n3. Add public key to GitHub:")
    print("   a) Run: cat ~/.ssh/id_ed25519.pub")
    print("   b) Copy the output")
    print("   c) Go to: https://github.com/settings/keys")
    print("   d) Click 'New SSH key'")
    print("   e) Paste and save")
    
    print("\n4. Update remote to use SSH:")
    git_exe = r'C:\Program Files\Git\cmd\git.exe'
    code, out, err = run_command(
        f'"{git_exe}" remote set-url origin git@github.com:rajnishchp/Bankingbot.git',
        cwd=repo_path
    )
    
    print("\n5. Push to GitHub:")
    input("Press Enter when SSH keys are configured...")
    
    code, out, err = run_command(
        f'"{git_exe}" push -u origin master',
        cwd=repo_path
    )
    
    if code == 0:
        print("\n✓ Successfully pushed to GitHub!")
    else:
        print(f"\nPush output: {out}")
        if err:
            print(f"Error: {err}")


def main():
    """Main function"""
    print()
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  Banking Bot - GitHub Push Helper".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    print("This tool will help you authenticate and push your Banking Bot to GitHub\n")
    
    repo_path = r"C:\Users\rajni\Tourism_Bot\banking_bot"
    
    # Check git status
    git_exe = r'C:\Program Files\Git\cmd\git.exe'
    code, status, _ = run_command(
        f'"{git_exe}" status',
        cwd=repo_path
    )
    
    print("Current Status:")
    print("-" * 70)
    print(status)
    print("-" * 70)
    
    setup_github_auth()


if __name__ == "__main__":
    main()
