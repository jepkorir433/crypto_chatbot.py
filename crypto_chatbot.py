def analyze_investment(risk, sustainable):
    """Generate crypto recommendations based on user preferences."""
    low_risk_coins = ["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)"]
    high_risk_coins = ["Solana (SOL)", "Polygon (MATIC)", "Avalanche (AVAX)"]
    sustainable_coins = ["Cardano (ADA)", "Algorand (ALGO)", "Tezos (XTZ)"]
    
    print("\nAnalyzing the best cryptocurrency investments for your profile...")
    
    # Risk-based recommendations
    if risk == "low":
        print("\n🔹 Recommended LOW-RISK Cryptocurrencies:")
        for coin in low_risk_coins:
            print(f"- {coin}")
    else:
        print("\n🔹 Recommended HIGH-RISK Cryptocurrencies:")
        for coin in high_risk_coins:
            print(f"- {coin}")
    
    # Sustainability filter
    if sustainable == "yes":
        print("\n🌱 Eco-Friendly Options:")
        for coin in sustainable_coins:
            if (risk == "low" and coin in low_risk_coins) or (risk == "high" and coin in high_risk_coins):
                print(f"- {coin} (Already listed above)")
            else:
                print(f"- {coin}")

def save_preferences(name, risk, sustainable):
    """Save user data to a text file."""
    with open("user_preferences.txt", "a") as file:
        file.write(f"{name}|{risk}|{sustainable}\n")

def load_recent_users():
    """Display recently saved profiles."""
    try:
        with open("user_preferences.txt", "r") as file:
            lines = file.readlines()[-3:]  # Last 3 entries
            if lines:
                print("\n📝 Recent Users:")
                for line in lines:
                    name, risk, sustainable = line.strip().split("|")
                    print(f"- {name} (Risk: {risk}, Sustainable: {sustainable})")
    except FileNotFoundError:
        pass

def main():
    print("Hi, I'm CryptoSage - your friendly crypto investment advisor!")
    
    while True:
        # Get user input
        name = input("\nWhat's your name? ").strip()
        while True:
            risk = input("Do you prefer high or low risk investments? (high/low): ").lower()
            if risk in ["high", "low"]:
                break
            print("Please enter 'high' or 'low'")
        
        while True:
            sustainable = input("Do you care about sustainability in crypto? (yes/no): ").lower()
            if sustainable in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'")

        # Generate recommendations
        analyze_investment(risk, sustainable)
        save_preferences(name, risk, sustainable)
        load_recent_users()

        # Continue or exit
        while True:
            choice = input("\nWould you like to analyze another profile? (yes/no): ").lower()
            if choice in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'")
        
        if choice == "no":
            print("\nThanks for using CryptoSage! Happy investing! 🚀")
            break

if __name__ == "__main__":
    main()
