from manager import PortfolioWorkflow

def main():
    # Initialize workflow manager
    manager = PortfolioWorkflow()

    # Option 1: Enter portfolio data manually
    print("Enter your portfolio data (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    portfolio_data = "\n".join(lines)

    # Option 2: Use sample data (uncomment to test quickly)
    """
    portfolio_data = '''
    | Asset   | Quantity | Purchase Price | Current Value |
    |---------|----------|----------------|---------------|
    | Apple   | 10       | 1500           | 1800          |
    | Google  | 20       | 2000           | 2100          |
    | TCS     | 15       | 1700           | 1900          |
    | Maruti  | 5        | 1200           | 1000          |
    '''
    """

    # Run manager synchronously
    results = manager.run_sync(portfolio_data)

    # Print results
    print("\n=== Portfolio Workflow Results ===\n")
    for section, value in results.items():
        print(f"--- {section} ---\n{value}\n")

if __name__ == "__main__":
    main()
