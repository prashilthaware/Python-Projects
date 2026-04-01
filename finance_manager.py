class FinanceManager:
    def __init__(self):
        self.income = 0
        self.expenses = {}

    def add_income(self, amount):
        self.income += amount
        print(f"Income added: ${amount:.2f}")

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"Expense added: ${amount:.2f} ({category})")

    def view_balance(self):
        total_expenses = sum(self.expenses.values())
        balance = self.income - total_expenses
        print(f"Income: ${self.income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

    def view_expenses(self):
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(f"- {category}: ${amount:.2f}")

def main():
    finance_manager = FinanceManager()

    while True:
        print("\nPersonal Finance Manager")
        print("1. Add income")
        print("2. Add expense")
        print("3. View balance")
        print("4. View expenses")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: $"))
            finance_manager.add_income(amount)
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: $"))
            finance_manager.add_expense(category, amount)
        elif choice == "3":
            finance_manager.view_balance()
        elif choice == "4":
            finance_manager.view_expenses()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()