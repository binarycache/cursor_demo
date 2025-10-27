"""Ethereum value converter between Wei, Gwei, and ETH."""

from dataclasses import dataclass
from typing import Literal

Unit = Literal["wei", "gwei", "eth"]


@dataclass
class EthereumValue:
    """Represents an Ethereum value in all three formats."""

    wei: str
    gwei: str
    eth: str

    def __str__(self) -> str:
        """Return formatted string representation."""
        return f"Wei: {self.wei}\nGwei: {self.gwei}\nETH: {self.eth}"


class EthereumConverter:
    """Convert Ethereum values between Wei, Gwei, and ETH."""

    WEI_PER_GWEI = 1_000_000_000  # 10^9
    WEI_PER_ETH = 1_000_000_000_000_000_000  # 10^18
    GWEI_PER_ETH = 1_000_000_000  # 10^9

    @classmethod
    def convert(cls, amount: str | int | float, unit: Unit) -> EthereumValue:
        """Convert an amount in specified unit to all three formats.

        Args:
            amount: The amount to convert (can be string, int, or float)
            unit: The unit of the input amount ("wei", "gwei", or "eth")

        Returns:
            EthereumValue object containing the value in all three formats

        Raises:
            ValueError: If unit is not recognized or if conversion fails
        """
        # Validate unit
        valid_units = ("wei", "gwei", "eth")
        if unit.lower() not in valid_units:
            raise ValueError(f"Unit must be one of {valid_units}")

        # Convert amount to string to handle large integers
        amount_str = str(amount)
        amount_float = float(amount_str)

        # Convert input to Wei first (canonical format)
        if unit.lower() == "wei":
            wei_value = int(amount_str)  # Keep as int for precision
        elif unit.lower() == "gwei":
            wei_value = int(amount_float * cls.WEI_PER_GWEI)
        elif unit.lower() == "eth":
            wei_value = int(amount_float * cls.WEI_PER_ETH)
        else:
            raise ValueError(f"Invalid unit: {unit}")

        # Convert to Gwei
        gwei_value = wei_value / cls.WEI_PER_GWEI

        # Convert to ETH
        eth_value = wei_value / cls.WEI_PER_ETH

        # Format with appropriate precision
        return EthereumValue(
            wei=str(wei_value),
            gwei=cls._format_decimal(gwei_value),
            eth=cls._format_decimal(eth_value),
        )

    @staticmethod
    def _format_decimal(value: float, decimals: int = 18) -> str:
        """Format a decimal value with appropriate precision.

        Args:
            value: The value to format
            decimals: Maximum number of decimal places

        Returns:
            Formatted string
        """
        # Remove trailing zeros
        formatted = f"{value:.{decimals}f}".rstrip("0").rstrip(".")
        return formatted if formatted else "0"


def convert(amount: str | int | float, unit: Unit) -> EthereumValue:
    """Convenience function to convert Ethereum values.

    Args:
        amount: The amount to convert
        unit: The unit of the input amount

    Returns:
        EthereumValue object with values in all three formats

    Example:
        >>> result = convert(1, "eth")
        >>> print(result.wei)
        1000000000000000000
    """
    return EthereumConverter.convert(amount, unit)


if __name__ == "__main__":
    import sys

    # Example usage
    examples = [
        (1, "eth"),
        (1000, "gwei"),
        ("1000000000000000000", "wei"),
        (0.5, "eth"),
        ("1500000000", "wei"),  # 1.5 Gwei
    ]

    print("Ethereum Value Converter\n" + "=" * 50)
    for amount, unit in examples:
        try:
            result = convert(amount, unit)
            print(f"\nInput: {amount} {unit.upper()}")
            print(result)
        except Exception as e:
            print(f"\nError converting {amount} {unit}: {e}")

    # Command line usage
    if len(sys.argv) == 3:
        try:
            amount = sys.argv[1]
            unit = sys.argv[2]
            result = convert(amount, unit)
            print(f"\nConverted: {amount} {unit.upper()}")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
            print("\nUsage: python eth_converter.py <amount> <unit>")
            print("Example: python eth_converter.py 1 eth")
            print("Example: python eth_converter.py 1000000000000000000 wei")

