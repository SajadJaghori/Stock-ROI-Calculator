def calculate_trade_outcome(investment_amount, current_price, percentage_change):
    # Calculate the outcome
    outcome = investment_amount * (1 + percentage_change / 100)
    
    # Calculate the number of shares
    num_shares = investment_amount / current_price
    
    return outcome, num_shares

# Get user input
investment_amount = float(input("Enter your investment amount: $"))
current_price = float(input("Enter the current price per share: $"))
percentage_change = float(input("Enter the percentage change: %"))

# Calculate outcome and number of shares
outcome, num_shares = calculate_trade_outcome(investment_amount, current_price, percentage_change)

# Display results
print(f"\nOutcome: ${outcome:.2f}")
print(f"Number of shares: {num_shares:.2f}")
