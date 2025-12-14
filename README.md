# Banking Bot - Powered by Mistral AI

A sophisticated banking assistance chatbot built with Mistral AI that handles customer inquiries, account management, and transaction processing.

## Features

- **Intelligent Chat Interface**: Natural language conversations powered by Mistral AI
- **Account Management**: Check balances, view account details
- **Transaction History**: View recent transactions for any account
- **Fund Transfers**: Transfer money between accounts
- **Banking Commands**: Quick commands for common banking operations
- **Conversation History**: Maintains context across multiple messages
- **Secure Design**: Best practices for banking security

## Project Structure

```
banking_bot/
├── src/
│   ├── __init__.py
│   └── banking_bot.py      # Main bot module
├── .env                     # Environment variables (API key)
├── requirements.txt         # Python dependencies
├── demo.py                  # Demo script showing all features
└── README.md               # This file
```

## Prerequisites

- Python 3.8 or higher
- Mistral AI API key (get one from [console.mistral.ai](https://console.mistral.ai))

## Setup Instructions

### 1. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

Navigate to the banking_bot directory and run:

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

The `.env` file already contains your API key. If you need to update it:

```bash
# Edit .env file
MISTRAL_API_KEY=your_api_key_here
```

Or set it as an environment variable:

```powershell
$env:MISTRAL_API_KEY="your_api_key_here"
```

## Usage

### Interactive Chat Mode

Run the bot in interactive mode:

```bash
python -m src.banking_bot
```

Then interact with the bot:
```
You: balance ACC001
Bot: Account ACC001 balance: $5000.00

You: What are your services?
Bot: [Mistral AI provides detailed response]
```

### Run Demo Script

See all features in action:

```bash
python demo.py
```

### Programmatic Usage

Use the bot in your own Python code:

```python
from src.banking_bot import BankingBot

# Initialize bot
bot = BankingBot(api_key="your_api_key")

# Check balance
balance = bot.get_account_balance("ACC001")
print(f"Balance: ${balance:.2f}")

# Chat with bot
response = bot.chat("What's my account balance?")
print(response)

# Transfer funds
result = bot.transfer_funds("ACC001", "ACC002", 100.00)
print(result)

# Get transaction history
history = bot.get_transaction_history("ACC001", limit=5)
for txn in history["transactions"]:
    print(f"{txn['date']}: {txn['type']} ${txn['amount']}")
```

## Available Commands

When running the bot interactively:

| Command | Description | Example |
|---------|-------------|---------|
| `balance <account_id>` | Check account balance | `balance ACC001` |
| `history <account_id>` | View transaction history | `history ACC001` |
| `transfer <from> <to> <amount>` | Transfer funds | `transfer ACC001 ACC002 500` |
| `reset` | Clear conversation history | `reset` |
| `exit` | Exit the bot | `exit` |

Or simply type any banking question in natural language!

## Mock Accounts for Testing

Two sample accounts are pre-configured:

| Account | Holder | Type | Balance |
|---------|--------|------|---------|
| ACC001 | John Doe | Checking | $5,000.00 |
| ACC002 | Jane Smith | Savings | $15,000.00 |

## API Details

### BankingBot Class Methods

#### `__init__(api_key: str = None)`
Initialize the bot with optional API key override.

#### `chat(user_message: str) -> str`
Send a message and get an AI-powered response.

#### `get_account_balance(account_id: str) -> float`
Retrieve the balance for an account.

#### `get_account_info(account_id: str) -> dict`
Get detailed account information.

#### `get_transaction_history(account_id: str, limit: int = 5) -> dict`
Retrieve recent transaction history.

#### `transfer_funds(from_account: str, to_account: str, amount: float) -> dict`
Transfer funds between accounts.

#### `process_banking_command(command: str) -> str`
Process banking-specific commands or chat messages.

#### `reset_conversation()`
Clear the conversation history.

## Model Configuration

The bot uses **mistral-small** model for fast, efficient responses. You can modify the model in the code:

```python
bot.model = "mistral-medium"  # or other available models
```

Available Mistral models:
- `mistral-small` - Fast, efficient (default)
- `mistral-medium` - Balanced
- `mistral-large` - Most capable

## Error Handling

The bot gracefully handles:
- Missing API keys
- Network errors
- Invalid account IDs
- Insufficient funds for transfers
- Mistral API failures (with fallback to REST API)

## Security Considerations

- **Never commit API keys to version control** - Use `.env` files
- The bot never stores sensitive information like passwords
- Always use HTTPS for API communication
- Implement additional authentication in production

## Troubleshooting

### "MISTRAL_API_KEY not found"
Ensure your `.env` file is in the same directory as the script and contains:
```
MISTRAL_API_KEY=your_key_here
```

### API Connection Errors
- Verify your internet connection
- Check if your API key is valid
- Ensure Mistral AI service is accessible

### Module Import Errors
Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

## Future Enhancements

- [ ] Multi-language support
- [ ] Voice interface integration
- [ ] Real database backend
- [ ] Advanced fraud detection
- [ ] Bill payment processing
- [ ] Loan application workflow
- [ ] Integration with real banking APIs
- [ ] User authentication and authorization
- [ ] Transaction scheduling
- [ ] Budget tracking and analytics

## License

This project is provided as-is for educational purposes.

## Support

For issues with:
- **Mistral AI API**: Visit [Mistral AI Docs](https://docs.mistral.ai)
- **This bot code**: Check the demo.py for usage examples

---

**Enjoy your Banking Bot! 🏦**
