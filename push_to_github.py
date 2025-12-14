#!/usr/bin/env python
"""
Push Banking Bot to GitHub using Git commands
Handles git initialization, configuration, and push to remote repository
"""

import os
import subprocess
import sys
from pathlib import Path

def run_git_command(cmd, cwd=None):
    """Run a git command and return output"""
    git_exe = r'C:\Program Files\Git\cmd\git.exe'
    full_cmd = f'"{git_exe}" {cmd}'
    
    try:
        result = subprocess.run(
            full_cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            shell=True
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def push_to_github():
    """Push banking bot code to GitHub repository"""
    
    # Configuration
    repo_path = r"C:\Users\rajni\Tourism_Bot\banking_bot"
    github_url = "https://github.com/rajnishchp/Bankingbot.git"
    username = "rajnishchp"
    email = "rajnishchp@gmail.com"
    
    print("=" * 70)
    print("Banking Bot - GitHub Push")
    print("=" * 70)
    
    try:
        # Initialize repo if needed
        if not Path(repo_path, ".git").exists():
            print(f"Initializing git repository at {repo_path}...")
            code, _, err = run_git_command("init", cwd=repo_path)
            if code != 0:
                print(f"✗ Failed to init: {err}")
                return False
            print("✓ Git repository initialized")
        else:
            print(f"✓ Git repository exists at {repo_path}")
        
        # Configure git user
        print(f"\nConfiguring git user:")
        print(f"  Name: {username}")
        print(f"  Email: {email}")
        
        run_git_command(f'config user.name "{username}"', cwd=repo_path)
        run_git_command(f'config user.email "{email}"', cwd=repo_path)
        print("✓ Git user configured")
        
        # Create .gitignore if not exists
        gitignore_path = Path(repo_path) / ".gitignore"
        if not gitignore_path.exists():
            print("\nCreating .gitignore...")
            gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.venv/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
"""
            gitignore_path.write_text(gitignore_content)
            print("✓ .gitignore created")
        
        # Stage all files
        print("\nStaging files...")
        code, out, err = run_git_command("add -A", cwd=repo_path)
        if code != 0:
            print(f"✗ Failed to stage: {err}")
            return False
        print("✓ All files staged")
        
        # Check status
        code, status, _ = run_git_command("status", cwd=repo_path)
        print(f"\nGit Status:\n{status}\n")
        
        # Create commit
        code, out, err = run_git_command(
            'commit -m "Initial commit: Banking Bot powered by Mistral AI"',
            cwd=repo_path
        )
        
        if code == 0:
            print("✓ Initial commit created")
        elif "nothing to commit" in err.lower() or "nothing to commit" in out.lower():
            print("! No changes to commit")
        else:
            print(f"✗ Commit failed: {err}")
        
        # Check if remote exists
        code, remotes, _ = run_git_command("remote -v", cwd=repo_path)
        
        if "origin" in remotes:
            print(f"\n✓ Remote 'origin' already configured")
        else:
            print(f"\nAdding remote repository: {github_url}")
            code, _, err = run_git_command(f'remote add origin "{github_url}"', cwd=repo_path)
            if code != 0:
                print(f"✗ Failed to add remote: {err}")
                return False
            print("✓ Remote 'origin' created")
        
        # Push to GitHub
        print("\nAttempting to push to GitHub...")
        print("Note: You'll need to authenticate with GitHub\n")
        
        # Try pushing with master branch
        code, out, err = run_git_command("push -u origin master", cwd=repo_path)
        
        if code == 0:
            print("✓ Successfully pushed to GitHub!")
        elif "fatal" in err.lower() and "repository not found" in err.lower():
            print("✗ Repository not found on GitHub")
            print(f"Please make sure the repository exists at: https://github.com/rajnishchp/Bankingbot")
            return False
        elif "fatal" in err.lower() and "could not read" in err.lower():
            print("✗ Authentication required")
            print("\nTo push, you have these options:")
            print("\n1. Using Personal Access Token (Recommended):")
            print(f"   git remote set-url origin https://<PAT>@github.com/rajnishchp/Bankingbot.git")
            print(f"   git push -u origin master")
            print("\n2. Using SSH:")
            print("   a) Generate SSH key (if not already done):")
            print("      ssh-keygen -t ed25519 -C 'rajnishchp@gmail.com'")
            print("   b) Add to GitHub: https://github.com/settings/keys")
            print(f"   c) git remote set-url origin git@github.com:rajnishchp/Bankingbot.git")
            print(f"   d) git push -u origin master")
            print("\n3. Use GitHub CLI:")
            print("   a) Download from https://cli.github.com")
            print("   b) Run: gh auth login")
            print("   c) Run: git push -u origin master")
            return False
        else:
            print(f"Push error: {err}")
            print(f"Output: {out}")
            return False
        
        print("\n" + "=" * 70)
        print("✓ Banking Bot pushed to GitHub successfully!")
        print("=" * 70)
        print(f"\nRepository: https://github.com/rajnishchp/Bankingbot")
        print(f"Local Path: {repo_path}")
        
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = push_to_github()
    sys.exit(0 if success else 1)
