# Quick Start Guide - Banking Bot

## One-Time Setup (First Time Only)

### 1. Activate Virtual Environment

```powershell
cd c:\Users\rajni\Tourism_Bot
& .\.venv\Scripts\Activate.ps1
cd banking_bot
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

Then run the activation command again.

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

## Running the Bot

### Option 1: Interactive Chat Mode (Recommended for Testing)

```powershell
python -m src.banking_bot
```

Then type your queries:
```
You: balance ACC001
Bot: Account ACC001 balance: $5000.00

You: What are your services?
Bot: [Mistral AI responds with detailed information]
```

**Available Commands:**
- `balance ACC001` - Check account balance
- `history ACC001` - View transaction history  
- `transfer ACC001 ACC002 500` - Transfer $500
- `reset` - Clear conversation
- `exit` - Quit

### Option 2: Run Demo Script

See all features automatically:

```powershell
python demo.py
```

This will:
✓ Check account balances
✓ Show account information
✓ Display transaction history
✓ Perform a fund transfer
✓ Have multiple AI conversations
✓ Execute banking commands

## Using the Bot in Your Code

```python
from src.banking_bot import BankingBot

bot = BankingBot()

# Check balance
balance = bot.get_account_balance("ACC001")
print(f"Balance: ${balance:.2f}")

# Chat
response = bot.chat("What's my account status?")
print(response)

# Transfer
result = bot.transfer_funds("ACC001", "ACC002", 100)
print(result)
```

## Test Accounts

| ID | Name | Type | Balance |
|----|------|------|---------|
| ACC001 | John Doe | Checking | $5,000 |
| ACC002 | Jane Smith | Savings | $15,000 |

## Troubleshooting

**Issue:** "Cannot find module src.banking_bot"
- **Solution:** Make sure you're running from the `banking_bot` directory

**Issue:** "MISTRAL_API_KEY not found"
- **Solution:** Check `.env` file contains your API key

**Issue:** Execution policy error
- **Solution:** Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force`

**Issue:** "No module named 'mistralai'"
- **Solution:** Run `pip install -r requirements.txt` again

## Project Location

```
c:\Users\rajni\Tourism_Bot\
├── .venv\                    (Virtual environment)
└── banking_bot\              (Project directory)
    ├── src\
    │   ├── __init__.py
    │   └── banking_bot.py    (Main bot code)
    ├── .env                  (API key - already configured)
    ├── requirements.txt      (Dependencies)
    ├── demo.py              (Demo script)
    └── README.md            (Full documentation)
```

## Next Steps

1. ✓ Virtual environment created
2. ✓ Bot installed and tested
3. → Try interactive mode: `python -m src.banking_bot`
4. → Customize the bot (add more accounts, features, etc.)
5. → Integrate into your application

---

**Happy Banking! 🏦**
