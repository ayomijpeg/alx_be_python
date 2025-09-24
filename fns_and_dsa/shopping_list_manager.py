def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' added to your shopping list.")
            else:
                print("⚠️ Item cannot be empty.")

        elif choice == '2':
            # Remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the list.")

        elif choice == '3':
            # View shopping list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("📭 Your shopping list is empty.")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
