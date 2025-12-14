"""
Advanced usage examples for the Banking Bot
Shows different ways to use the bot in your applications
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from banking_bot import BankingBot


def example_1_basic_chat():
    """Example 1: Basic chat functionality"""
    print("\n" + "="*60)
    print("Example 1: Basic Chat Functionality")
    print("="*60)
    
    bot = BankingBot()
    
    # Single question
    response = bot.chat("What are the benefits of a savings account?")
    print(f"Q: What are the benefits of a savings account?")
    print(f"A: {response}\n")


def example_2_account_operations():
    """Example 2: Account operations"""
    print("\n" + "="*60)
    print("Example 2: Account Operations")
    print("="*60)
    
    bot = BankingBot()
    
    # Get balance
    balance = bot.get_account_balance("ACC001")
    print(f"Balance for ACC001: ${balance:.2f}")
    
    # Get full account info
    info = bot.get_account_info("ACC002")
    print(f"\nAccount Holder: {info['account_holder']}")
    print(f"Account Type: {info['account_type']}")
    print(f"Balance: ${info['balance']:.2f}")


def example_3_transactions():
    """Example 3: Working with transactions"""
    print("\n" + "="*60)
    print("Example 3: Transaction Management")
    print("="*60)
    
    bot = BankingBot()
    
    # View transaction history
    history = bot.get_transaction_history("ACC001", limit=5)
    print(f"Recent transactions for ACC001:")
    for txn in history["transactions"]:
        print(f"  {txn['date']}: {txn['type'].upper():10} ${txn['amount']:8.2f} - {txn['description']}")
    
    # Perform transfer
    print("\nPerforming transfer...")
    result = bot.transfer_funds("ACC002", "ACC001", 250.00)
    if result.get("success"):
        print(f"✓ {result['message']}")
    else:
        print(f"✗ {result.get('error')}")
    
    # View updated balance
    new_balance = bot.get_account_balance("ACC002")
    print(f"Updated ACC002 balance: ${new_balance:.2f}")


def example_4_conversational_flow():
    """Example 4: Multi-turn conversation"""
    print("\n" + "="*60)
    print("Example 4: Multi-turn Conversation")
    print("="*60)
    
    bot = BankingBot()
    
    # This conversation shows the bot maintaining context
    conversation = [
        "I want to open a new account",
        "What documents do I need?",
        "What are the fees?",
        "How long does the process take?"
    ]
    
    for question in conversation:
        print(f"\nYou: {question}")
        response = bot.chat(question)
        # Print first 200 chars of response for brevity
        preview = response[:200] + "..." if len(response) > 200 else response
        print(f"Bot: {preview}")


def example_5_error_handling():
    """Example 5: Error handling and edge cases"""
    print("\n" + "="*60)
    print("Example 5: Error Handling")
    print("="*60)
    
    bot = BankingBot()
    
    # Invalid account
    print("Checking invalid account...")
    balance = bot.get_account_balance("ACC999")
    print(f"Result: {balance}")
    
    # Insufficient funds
    print("\nAttempting transfer with insufficient funds...")
    result = bot.transfer_funds("ACC001", "ACC002", 999999.00)
    print(f"Result: {result}")
    
    # Getting account info for non-existent account
    print("\nGetting info for non-existent account...")
    info = bot.get_account_info("ACC999")
    print(f"Result: {info}")


def example_6_command_processing():
    """Example 6: Direct command processing"""
    print("\n" + "="*60)
    print("Example 6: Banking Commands")
    print("="*60)
    
    bot = BankingBot()
    
    commands = [
        ("balance ACC001", "Check balance"),
        ("history ACC002", "View history"),
        ("transfer ACC001 ACC002 100", "Transfer funds"),
    ]
    
    for cmd, description in commands:
        print(f"\n{description}:")
        print(f"Command: {cmd}")
        result = bot.process_banking_command(cmd)
        print(f"Result: {result}")


def example_7_custom_integration():
    """Example 7: Integrating into a larger system"""
    print("\n" + "="*60)
    print("Example 7: System Integration")
    print("="*60)
    
    # Simulating a banking application
    class BankingApplication:
        def __init__(self):
            self.bot = BankingBot()
        
        def customer_inquiry(self, customer_id, inquiry):
            """Handle customer inquiry"""
            response = self.bot.chat(inquiry)
            return {
                "customer_id": customer_id,
                "inquiry": inquiry,
                "response": response,
                "timestamp": "2024-12-14"
            }
        
        def generate_account_report(self, account_id):
            """Generate account report"""
            account = self.bot.get_account_info(account_id)
            history = self.bot.get_transaction_history(account_id, limit=10)
            
            return {
                "account_id": account_id,
                "account_info": account,
                "recent_transactions": history["transactions"],
                "account_status": "Active"
            }
    
    # Use the application
    app = BankingApplication()
    
    # Handle inquiry
    inquiry_result = app.customer_inquiry("CUST001", "How can I improve my credit score?")
    print(f"Customer: {inquiry_result['customer_id']}")
    print(f"Inquiry: {inquiry_result['inquiry']}")
    print(f"Response: {inquiry_result['response'][:150]}...\n")
    
    # Generate report
    report = app.generate_account_report("ACC001")
    print(f"Report for {report['account_id']}:")
    print(f"  Status: {report['account_status']}")
    print(f"  Holder: {report['account_info']['account_holder']}")
    print(f"  Balance: ${report['account_info']['balance']:.2f}")
    print(f"  Recent transactions: {len(report['recent_transactions'])}")


def example_8_session_management():
    """Example 8: Managing conversation sessions"""
    print("\n" + "="*60)
    print("Example 8: Session Management")
    print("="*60)
    
    bot = BankingBot()
    
    print("Conversation Session 1:")
    print("-" * 40)
    bot.chat("Tell me about overdraft protection")
    bot.chat("What are the costs?")
    response = bot.chat("So should I enable it?")
    print(f"Response (with context): {response[:150]}...")
    
    # Reset conversation
    print("\nClearing conversation history...")
    bot.reset_conversation()
    
    print("\nConversation Session 2 (fresh start):")
    print("-" * 40)
    response = bot.chat("Tell me about overdraft protection")
    print(f"Response (no context): {response[:150]}...")


if __name__ == "__main__":
    print("\n🏦 Banking Bot - Advanced Usage Examples")
    print("Run individual examples or modify as needed\n")
    
    # Run all examples
    try:
        example_1_basic_chat()
        example_2_account_operations()
        example_3_transactions()
        example_4_conversational_flow()
        example_5_error_handling()
        example_6_command_processing()
        example_7_custom_integration()
        example_8_session_management()
        
        print("\n" + "="*60)
        print("✓ All examples completed successfully!")
        print("="*60 + "\n")
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
