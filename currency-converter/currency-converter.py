from forex_python.converter import CurrencyRates

# Function to convert currencies
def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    rate = c.get_rates(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount

# Example usage
amount = 100  # Amount to be converted
from_currency = 'USD'  # Source currency
to_currency = 'EUR'  # Target currency

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
