#!/usr/bin/env python3
"""
shopping_list_manager.py

Simple interactive shopping list manager using a Python list.
Features:
- Add items
- Remove items
- View current list
- Exit
"""

shopping_list = []

def add_item(item: str) -> None:
	"""Append an item to the shopping_list if non-empty."""
	item = item.strip()
	if not item:
		print("Cannot add an empty item.")
		return
	shopping_list.append(item)
	print(f"Added: {item}")

def remove_item(item: str) -> None:
	"""Remove the first occurrence of item from shopping_list if present."""
	item = item.strip()
	if not item:
		print("Please provide an item name to remove.")
		return
	try:
		shopping_list.remove(item)
		print(f"Removed: {item}")
	except ValueError:
		print(f"Item not found: {item}")

def view_list() -> None:
	"""Print current shopping list items, or a message if empty."""
	if not shopping_list:
		print("Shopping list is empty.")
		return
	print("Shopping list:")
	for idx, item in enumerate(shopping_list, start=1):
		print(f"{idx}. {item}")
		
def display_menu():
	print("Shopping List Manager")
	print("1. Add item")
	print("2. Remove item")	
	print("3. View list")	
	print("4. Exit")    

def main() -> None:
	"""Interactive menu loop."""
	menu = (
		"\nShopping List Manager\n"
		"1. Add item\n"
		"2. Remove item\n"
		"3. View list\n"
		"4. Exit\n"
		"Choose an option (1-4): "
	)

	while True:
		choice = input(menu).strip()
		if choice == "1":
			item = input("Enter the item to add: ")
			add_item(item)
		elif choice == "2":
			item = input("Enter item to remove: ")
			remove_item(item)
		elif choice == "3":
			view_list()
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
	main()

