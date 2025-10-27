# Ethereum Value Converter

A Python utility for converting Ethereum values between Wei, Gwei, and ETH formats.

## Features

- Convert between Wei, Gwei, and ETH
- Supports string, int, and float inputs
- Preserves precision for large values
- Returns all three formats simultaneously
- Type-safe with proper type hints
- Comprehensive unit tests

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage

### As a Python Module

```python
from eth_converter import convert

# Convert 1 ETH to all formats
result = convert(1, "eth")
print(result.wei)   # "1000000000000000000"
print(result.gwei)  # "1000000000"
print(result.eth)   # "1"

# Convert 1000 Gwei
result = convert(1000, "gwei")
print(result)  # Prints all three formats

# Convert Wei
result = convert("1000000000000000000", "wei")
print(result.eth)  # "1"
```

### Command Line

```bash
python eth_converter.py <amount> <unit>

# Examples
python eth_converter.py 1 eth
python eth_converter.py 1000000000000000000 wei
python eth_converter.py 1000 gwei
```

## Conversion Rates

- 1 ETH = 1,000,000,000 Gwei (10^9)
- 1 ETH = 1,000,000,000,000,000,000 Wei (10^18)
- 1 Gwei = 1,000,000,000 Wei (10^9)

## Running Tests

```bash
# Run all tests
pytest test_eth_converter.py -v

# Run with coverage
pytest test_eth_converter.py --cov=eth_converter --cov-report=html
```

## API Reference

### `convert(amount, unit)`

Convert an Ethereum value to all three formats.

**Parameters:**
- `amount` (str | int | float): The amount to convert
- `unit` (Literal["wei", "gwei", "eth"]): The unit of the input amount

**Returns:**
- `EthereumValue`: Dataclass containing:
  - `wei` (str): Value in Wei
  - `gwei` (str): Value in Gwei
  - `eth` (str): Value in ETH

**Raises:**
- `ValueError`: If unit is not recognized

## Examples

```python
from eth_converter import convert

# Convert 1 ETH
result = convert(1, "eth")
print(f"1 ETH = {result.wei} Wei")
print(f"1 ETH = {result.gwei} Gwei")
print(f"1 ETH = {result.eth} ETH")

# Convert 0.5 ETH
result = convert(0.5, "eth")
print(result)

# Convert 1000 Gwei
result = convert(1000, "gwei")
print(result)
```

## License

MIT

