"""
Demo and test script for the Banking Bot
Shows how to use the bot programmatically
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from banking_bot import BankingBot


def run_demo():
    """Run a demo of the banking bot."""
    print("\n" + "=" * 60)
    print("Banking Bot - Demo & Test")
    print("=" * 60 + "\n")
    
    try:
        # Initialize bot
        bot = BankingBot()
        print("✓ Bot initialized successfully\n")
    except ValueError as e:
        print(f"✗ Initialization failed: {e}")
        return
    
    # Demo 1: Check balance
    print("Demo 1: Check Account Balance")
    print("-" * 40)
    balance = bot.get_account_balance("ACC001")
    print(f"Balance for ACC001: ${balance:.2f}\n")
    
    # Demo 2: Get account info
    print("Demo 2: Get Account Information")
    print("-" * 40)
    account_info = bot.get_account_info("ACC002")
    print(f"Account: {account_info['account_holder']}")
    print(f"Type: {account_info['account_type']}")
    print(f"Balance: ${account_info['balance']:.2f}\n")
    
    # Demo 3: Get transaction history
    print("Demo 3: Transaction History")
    print("-" * 40)
    history = bot.get_transaction_history("ACC001", limit=3)
    for txn in history["transactions"]:
        print(f"  {txn['date']}: {txn['type'].upper()} ${txn['amount']:.2f} - {txn['description']}")
    print()
    
    # Demo 4: Transfer funds
    print("Demo 4: Fund Transfer")
    print("-" * 40)
    result = bot.transfer_funds("ACC001", "ACC002", 500.00)
    if result.get("success"):
        print(f"✓ {result['message']}")
        print(f"  New balance: ${result['new_balance']:.2f}\n")
    else:
        print(f"✗ Transfer failed: {result.get('error')}\n")
    
    # Demo 5: Chat with bot about banking
    print("Demo 5: Chat with Banking Bot")
    print("-" * 40)
    
    questions = [
        "What are your services?",
        "How can I protect my account from fraud?",
        "What's the process for transferring money between accounts?",
    ]
    
    for question in questions:
        print(f"User: {question}")
        try:
            response = bot.chat(question)
            print(f"Bot: {response}\n")
        except Exception as e:
            print(f"Bot: Error - {str(e)}\n")
    
    # Demo 6: Process banking commands
    print("Demo 6: Banking Commands")
    print("-" * 40)
    
    commands = [
        "balance ACC002",
        "history ACC001",
    ]
    
    for cmd in commands:
        print(f"Command: {cmd}")
        result = bot.process_banking_command(cmd)
        print(f"Result: {result}\n")
    
    print("=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
