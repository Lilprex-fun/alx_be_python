#!/usr/bin/env python3
"""
explore_datetime.py

Demonstrates the use of the datetime module for handling dates and times.
Features:
- Display current date and time
- Calculate future date by adding days
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in a readable format.
    Saves the current date inside a current_date variable.
    Format: "YYYY-MM-DD HH:MM:SS"
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(days):
    """
    Calculate the date after adding the specified number of days.
    Saves the future date inside a future_date variable.
    Format: "YYYY-MM-DD"
    
    Args:
        days (int): Number of days to add to the current date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date ({days} days from now): {formatted_future}")
    return future_date


def main():
    """Interactive menu for datetime operations."""
    while True:
        print("\nDatetime Explorer")
        print("1. Display current date and time")
        print("2. Calculate future date")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            try:
                 days = int(input("Enter the number of days to add to the current date: "))
                 calculate_future_date(days)
            except ValueError:
                  print("Invalid input. Please enter an integer.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
