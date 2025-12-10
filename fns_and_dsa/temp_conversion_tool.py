#!/usr/bin/env python3
"""
temp_conversion_tool.py

Temperature conversion utilities and a small interactive prompt.

Defines global conversion factors and two conversion functions:
- convert_to_celsius(fahrenheit)
- convert_to_fahrenheit(celsius)

Interactive prompt asks for a temperature and its unit (C/F)
and prints the converted value.
"""

from typing import Union

# Global conversion factors
# Multiply by FAHRENHEIT_TO_CELSIUS_FACTOR after subtracting 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
# Multiply Celsius by CELSIUS_TO_FAHRENHEIT_FACTOR and add 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0


def convert_to_celsius(fahrenheit: Union[int, float]) -> float:
	"""Convert Fahrenheit to Celsius using the global factor.

	Formula: (F - 32) * (5/9)
	"""
	f = float(fahrenheit)
	return (f - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: Union[int, float]) -> float:
	"""Convert Celsius to Fahrenheit using the global factor.

	Formula: C * (9/5) + 32
	"""
	c = float(celsius)
	return c * CELSIUS_TO_FAHRENHEIT_FACTOR + 32.0


def _prompt_and_convert() -> None:
	"""Prompt the user for a temperature and unit, then convert and print result.

	If the temperature value is not numeric, raise ValueError with the
	exact message required by the spec.
	"""
	temp_str = input("Enter the temperature to convert: ").strip()
	try:
		temp_value = float(temp_str)
	except ValueError:
		raise ValueError("Invalid temperature. Please enter a numeric value.")

	unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
	if unit == "F":
		c = convert_to_celsius(temp_value)
		print(f"{temp_value}°F is {c}°C")
	elif unit == "C":
		f = convert_to_fahrenheit(temp_value)
		print(f"{temp_value}°C is {f}°F")
	else:
		print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


def main() -> None:
	"""Run a single conversion prompt. Guarded so imports don't trigger it."""
	try:
		_prompt_and_convert()
	except ValueError as e:
		# Re-raise so callers/scripts see the error as requested by the spec
		raise


if __name__ == "__main__":
	main()

