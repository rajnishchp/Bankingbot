# GitHub Push Setup Guide

Your Banking Bot code has been prepared for GitHub. Follow these steps to push it to your repository:

## Quick Option: Interactive Helper (Easiest)

```powershell
cd c:\Users\rajni\Tourism_Bot\banking_bot
python github_auth_helper.py
```

This will guide you through authentication step-by-step.

---

## Manual Options

### Option 1: GitHub CLI (Recommended)

**Advantages:** Easy, secure, integrated with GitHub

**Steps:**

1. **Install GitHub CLI:**
   ```powershell
   winget install GitHub.cli
   ```

2. **Authenticate with GitHub:**
   ```powershell
   gh auth login
   ```
   - Select: GitHub.com
   - Select: HTTPS
   - Authenticate with your browser

3. **Push to GitHub:**
   ```powershell
   cd c:\Users\rajni\Tourism_Bot\banking_bot
   & "C:\Program Files\Git\cmd\git.exe" push -u origin master
   ```

---

### Option 2: Personal Access Token (PAT)

**Advantages:** Fine-grained control, no app installation

**Steps:**

1. **Create Token on GitHub:**
   - Go to: https://github.com/settings/tokens
   - Click: "Generate new token" → "Generate new token (classic)"
   - Settings:
     - Note: `Banking Bot Push`
     - Expiration: 30 days
     - Scopes: ✓ repo (full control)
   - Click: "Generate token"
   - **Copy the token** (you won't see it again!)

2. **Configure Git with Token:**
   ```powershell
   cd c:\Users\rajni\Tourism_Bot\banking_bot
   
   $token = "ghp_xxxx..."  # Paste your token here
   $url = "https://${token}@github.com/rajnishchp/Bankingbot.git"
   
   & "C:\Program Files\Git\cmd\git.exe" remote set-url origin $url
   ```

3. **Push to GitHub:**
   ```powershell
   & "C:\Program Files\Git\cmd\git.exe" push -u origin master
   ```

4. **Secure the Remote (Optional but Recommended):**
   ```powershell
   & "C:\Program Files\Git\cmd\git.exe" remote set-url origin "https://github.com/rajnishchp/Bankingbot.git"
   ```

---

### Option 3: SSH Keys

**Advantages:** More secure for long-term use, no password needed

**Steps:**

1. **Generate SSH Key (if you don't have one):**
   ```powershell
   ssh-keygen -t ed25519 -C "rajnishchp@gmail.com"
   # Press Enter for default location
   # Enter a passphrase (recommended)
   ```

2. **Add to SSH Agent:**
   ```powershell
   # Start SSH agent
   ssh-agent -s
   
   # Add your key
   ssh-add "$env:USERPROFILE\.ssh\id_ed25519"
   ```

3. **Add Public Key to GitHub:**
   ```powershell
   # Copy the public key
   Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub" | Set-Clipboard
   
   # Go to https://github.com/settings/keys
   # Click "New SSH key"
   # Paste your key and save
   ```

4. **Configure Git Remote:**
   ```powershell
   cd c:\Users\rajni\Tourism_Bot\banking_bot
   & "C:\Program Files\Git\cmd\git.exe" remote set-url origin "git@github.com:rajnishchp/Bankingbot.git"
   ```

5. **Push to GitHub:**
   ```powershell
   & "C:\Program Files\Git\cmd\git.exe" push -u origin master
   ```

---

## Verify Push Success

After pushing, verify with:

```powershell
# Check remote status
& "C:\Program Files\Git\cmd\git.exe" remote -v

# Check push result
& "C:\Program Files\Git\cmd\git.exe" log --oneline
```

Or visit: https://github.com/rajnishchp/Bankingbot

---

## Troubleshooting

### Error: "Repository not found"
- Ensure the repository exists on GitHub
- Check the URL: `https://github.com/rajnishchp/Bankingbot`

### Error: "fatal: could not read Username"
- You need authentication (see options above)

### Error: "Permission denied (publickey)"
- SSH key setup issue
- Try PAT or GitHub CLI instead

### View Commit History
```powershell
cd c:\Users\rajni\Tourism_Bot\banking_bot
& "C:\Program Files\Git\cmd\git.exe" log --oneline -n 5
```

### Check Git Configuration
```powershell
& "C:\Program Files\Git\cmd\git.exe" config --list
```

---

## Next Steps

After successful push:

1. ✓ Code is on GitHub
2. ✓ Repository is public/accessible
3. Next: Add collaborators, set up CI/CD, or deploy

Visit your repository:
```
https://github.com/rajnishchp/Bankingbot
```

---

## Files Pushed

The following files have been committed and are ready to push:

```
banking_bot/
├── src/
│   ├── __init__.py
│   └── banking_bot.py           (500+ lines, fully documented)
├── .env                         (API key configured)
├── .gitignore                   (Proper Python exclusions)
├── requirements.txt             (All dependencies listed)
├── README.md                    (Full documentation)
├── QUICKSTART.md                (Setup guide)
├── PROJECT_SUMMARY.md           (Project overview)
├── demo.py                      (Demo script)
├── examples.py                  (8 usage examples)
├── main.py                      (Entry point)
├── push_to_github.py            (Git automation)
└── github_auth_helper.py        (Authentication helper)
```

---

**Your Banking Bot is ready for GitHub! 🚀**
