"""
Banking Bot using Mistral AI
Provides intelligent banking assistance with account management, transactions, and customer support
"""

import os
import json
from typing import Optional, Dict, Any
from datetime import datetime
from dotenv import load_dotenv

# Try importing mistralai, with fallback handling
try:
    from mistralai.client import MistralClient
    from mistralai.models.chat_message import ChatMessage
except ImportError:
    MistralClient = None
    ChatMessage = None

import requests

# Load environment variables
load_dotenv()

class BankingBot:
    """
    A banking assistance bot powered by Mistral AI.
    Handles customer inquiries about accounts, transactions, and banking services.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Banking Bot with Mistral AI client.
        
        Args:
            api_key: Mistral AI API key (defaults to MISTRAL_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY not found in environment variables or arguments")
        
        # Initialize Mistral client
        try:
            if MistralClient is not None:
                self.client = MistralClient(api_key=self.api_key)
            else:
                self.client = None
                self._use_rest_api = True
        except Exception as e:
            print(f"Warning: Could not initialize Mistral SDK client: {e}")
            self._use_rest_api = True
            self.client = None
        
        self.model = "mistral-small"
        self.conversation_history = []
        self.user_accounts = self._initialize_mock_accounts()
        
    def _initialize_mock_accounts(self) -> Dict[str, Dict[str, Any]]:
        """Initialize mock user accounts for demonstration."""
        return {
            "ACC001": {
                "account_holder": "John Doe",
                "balance": 5000.00,
                "account_type": "Checking",
                "transactions": [
                    {"date": "2024-12-10", "type": "deposit", "amount": 1000.00, "description": "Salary"},
                    {"date": "2024-12-08", "type": "withdrawal", "amount": 200.00, "description": "ATM"},
                ]
            },
            "ACC002": {
                "account_holder": "Jane Smith",
                "balance": 15000.00,
                "account_type": "Savings",
                "transactions": [
                    {"date": "2024-12-12", "type": "deposit", "amount": 500.00, "description": "Transfer"},
                ]
            }
        }
    
    def get_account_info(self, account_id: str) -> Dict[str, Any]:
        """Get account information."""
        if account_id in self.user_accounts:
            return self.user_accounts[account_id]
        return {"error": f"Account {account_id} not found"}
    
    def get_account_balance(self, account_id: str) -> float:
        """Get the balance of an account."""
        if account_id in self.user_accounts:
            return self.user_accounts[account_id]["balance"]
        return None
    
    def transfer_funds(self, from_account: str, to_account: str, amount: float) -> Dict[str, Any]:
        """Transfer funds between accounts."""
        if from_account not in self.user_accounts:
            return {"success": False, "error": f"Source account {from_account} not found"}
        
        if to_account not in self.user_accounts:
            return {"success": False, "error": f"Destination account {to_account} not found"}
        
        from_balance = self.user_accounts[from_account]["balance"]
        if from_balance < amount:
            return {"success": False, "error": "Insufficient funds"}
        
        self.user_accounts[from_account]["balance"] -= amount
        self.user_accounts[to_account]["balance"] += amount
        
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "type": "transfer",
            "amount": amount,
            "description": f"Transfer to {to_account}"
        }
        self.user_accounts[from_account]["transactions"].append(transaction)
        
        return {
            "success": True,
            "message": f"Transferred ${amount:.2f} from {from_account} to {to_account}",
            "new_balance": self.user_accounts[from_account]["balance"]
        }
    
    def get_transaction_history(self, account_id: str, limit: int = 5) -> Dict[str, Any]:
        """Get transaction history for an account."""
        if account_id not in self.user_accounts:
            return {"error": f"Account {account_id} not found"}
        
        transactions = self.user_accounts[account_id]["transactions"][-limit:]
        return {
            "account_id": account_id,
            "transactions": transactions
        }
    
    def _call_mistral_api_rest(self, messages: list) -> str:
        """Call Mistral AI using REST API directly."""
        url = "https://api.mistral.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error calling Mistral API: {str(e)}"
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt for the banking bot."""
        return """You are a helpful banking assistant powered by Mistral AI. You help customers with:
- Account information and balance inquiries
- Transaction history
- Fund transfers between accounts
- General banking questions
- Security and fraud prevention advice

Be professional, secure (never ask for sensitive data), and helpful. 
When users ask about specific accounts or transactions, acknowledge the information provided.
Always encourage secure banking practices."""
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to the banking bot and get a response.
        
        Args:
            user_message: The user's input message
            
        Returns:
            The bot's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Prepare messages for API call
        system_message = self._build_system_prompt()
        messages = [{"role": "system", "content": system_message}]
        messages.extend(self.conversation_history)
        
        try:
            # Try SDK first, fall back to REST API
            if self.client is not None and MistralClient is not None:
                try:
                    chat_messages = [ChatMessage(role=msg["role"], content=msg["content"]) for msg in messages]
                    response = self.client.chat(model=self.model, messages=chat_messages)
                    bot_response = response.choices[0].message.content
                except Exception as e:
                    print(f"SDK call failed, using REST API: {e}")
                    bot_response = self._call_mistral_api_rest(messages)
            else:
                bot_response = self._call_mistral_api_rest(messages)
            
            # Add bot response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": bot_response
            })
            
            return bot_response
            
        except Exception as e:
            error_response = f"Sorry, I encountered an error: {str(e)}"
            self.conversation_history.append({
                "role": "assistant",
                "content": error_response
            })
            return error_response
    
    def process_banking_command(self, command: str) -> str:
        """
        Process banking-specific commands.
        
        Args:
            command: The banking command to process
            
        Returns:
            The result of the command
        """
        if command.startswith("balance"):
            parts = command.split()
            if len(parts) > 1:
                account_id = parts[1]
                balance = self.get_account_balance(account_id)
                if balance is not None:
                    return f"Account {account_id} balance: ${balance:.2f}"
                else:
                    return f"Account {account_id} not found"
        
        elif command.startswith("transfer"):
            parts = command.split()
            if len(parts) >= 4:
                from_acc = parts[1]
                to_acc = parts[2]
                try:
                    amount = float(parts[3])
                    result = self.transfer_funds(from_acc, to_acc, amount)
                    if result.get("success"):
                        return result["message"]
                    else:
                        return result.get("error", "Transfer failed")
                except ValueError:
                    return "Invalid transfer amount"
        
        elif command.startswith("history"):
            parts = command.split()
            if len(parts) > 1:
                account_id = parts[1]
                result = self.get_transaction_history(account_id)
                if "error" not in result:
                    transactions = result["transactions"]
                    return f"Recent transactions for {account_id}:\n" + \
                           "\n".join([f"  {t['date']}: {t['type']} ${t['amount']:.2f} - {t['description']}" 
                                     for t in transactions])
                else:
                    return result["error"]
        
        # If not a specific command, treat as a chat message
        return self.chat(command)
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = []


def main():
    """Main function to run the banking bot."""
    print("=" * 60)
    print("Welcome to Banking Bot powered by Mistral AI")
    print("=" * 60)
    print("\nAvailable commands:")
    print("  balance <account_id>      - Check account balance")
    print("  history <account_id>      - View transaction history")
    print("  transfer <from> <to> <amount> - Transfer funds")
    print("  Or just type any banking question!")
    print("\nExample accounts: ACC001, ACC002")
    print("Type 'exit' to quit\n")
    
    try:
        bot = BankingBot()
        print("✓ Banking Bot initialized successfully\n")
    except ValueError as e:
        print(f"✗ Error: {e}")
        print("Please set MISTRAL_API_KEY environment variable")
        return
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print("\nThank you for using Banking Bot. Goodbye!")
                break
            
            if user_input.lower() == "reset":
                bot.reset_conversation()
                print("Conversation history cleared.\n")
                continue
            
            print("\nBot: ", end="", flush=True)
            response = bot.process_banking_command(user_input)
            print(response)
            print()
            
        except KeyboardInterrupt:
            print("\n\nThank you for using Banking Bot. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
