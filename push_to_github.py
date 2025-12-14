#!/usr/bin/env python
"""
Push Banking Bot to GitHub
Handles git initialization, configuration, and push to remote repository
"""

import os
import sys
from pathlib import Path

# Set Git executable path before importing git
os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = r'C:\Program Files\Git\cmd\git.exe'

from git import Repo, Actor

def push_to_github():
    """Push banking bot code to GitHub repository"""
    
    # Configuration
    repo_path = Path("c:/Users/rajni/Tourism_Bot/banking_bot")
    github_url = "https://github.com/rajnishchp/Bankingbot.git"
    username = "rajnishchp"
    email = "rajnishchp@gmail.com"
    
    print("=" * 70)
    print("Banking Bot - GitHub Push")
    print("=" * 70)
    
    try:
        # Check if repo already exists
        if (repo_path / ".git").exists():
            print(f"✓ Git repository already exists at {repo_path}")
            repo = Repo(repo_path)
        else:
            print(f"Creating git repository at {repo_path}...")
            repo = Repo.init(repo_path)
            print("✓ Git repository initialized")
        
        # Configure git user
        print(f"\nConfiguring git user:")
        print(f"  Name: {username}")
        print(f"  Email: {email}")
        
        with repo.config_writer() as git_config:
            git_config.set_value("user", "name", username)
            git_config.set_value("user", "email", email)
        
        print("✓ Git user configured")
        
        # Create .gitignore
        gitignore_path = repo_path / ".gitignore"
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

# Virtual Environment
.venv/
.venv

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
        repo.git.add(A=True)
        print("✓ All files staged")
        
        # Get status
        status = repo.git.status()
        print(f"\nGit Status:\n{status}\n")
        
        # Check if there are changes to commit
        if repo.is_dirty() or repo.untracked_files:
            # Create initial commit
            print("Creating initial commit...")
            actor = Actor(username, email)
            repo.index.commit(
                "Initial commit: Banking Bot powered by Mistral AI",
                author=actor,
                committer=actor
            )
            print("✓ Initial commit created")
        else:
            print("! No changes to commit")
        
        # Check remote
        remotes = [remote.name for remote in repo.remotes]
        
        if "origin" in remotes:
            print(f"\n✓ Remote 'origin' already configured: {repo.remote('origin').url}")
            # Update remote URL if different
            if repo.remote('origin').url != github_url:
                print(f"Updating remote URL to: {github_url}")
                repo.delete_remote("origin")
                repo.create_remote("origin", github_url)
        else:
            print(f"\nAdding remote repository: {github_url}")
            repo.create_remote("origin", github_url)
            print("✓ Remote 'origin' created")
        
        # Push to GitHub
        print("\nPushing to GitHub...")
        print("(This may prompt for authentication)")
        
        try:
            repo.remotes.origin.push()
            print("✓ Successfully pushed to GitHub!")
        except Exception as push_error:
            print(f"\n⚠ Push requires authentication")
            print(f"Error: {push_error}")
            print("\nTo authenticate, you can:")
            print("1. Use a Personal Access Token (PAT):")
            print(f"   URL: https://<token>@github.com/rajnishchp/Bankingbot.git")
            print("\n2. Use SSH:")
            print("   - Set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh")
            print("   - Change remote: git remote set-url origin git@github.com:rajnishchp/Bankingbot.git")
            print("\n3. Use GitHub CLI:")
            print("   - Install from https://cli.github.com")
            print("   - Run: gh auth login")
            return False
        
        print("\n" + "=" * 70)
        print("✓ Successfully pushed Banking Bot to GitHub!")
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
    os.chdir("c:/Users/rajni/Tourism_Bot")
    success = push_to_github()
    sys.exit(0 if success else 1)
