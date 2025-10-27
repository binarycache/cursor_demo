"""Tests for Ethereum value converter."""

import pytest
from eth_converter import convert, EthereumValue, EthereumConverter


class TestEthereumConverter:
    """Test cases for Ethereum conversion."""

    def test_wei_to_all(self) -> None:
        """Test conversion from Wei."""
        result = convert(1_000_000_000, "wei")
        assert result.wei == "1000000000"
        assert float(result.gwei) == 1.0
        assert float(result.eth) == 0.000000001

    def test_gwei_to_all(self) -> None:
        """Test conversion from Gwei."""
        result = convert(1, "gwei")
        assert result.wei == "1000000000"
        assert result.gwei == "1"
        assert result.eth == "0.000000001"

    def test_eth_to_all(self) -> None:
        """Test conversion from ETH."""
        result = convert(1, "eth")
        assert result.wei == "1000000000000000000"
        assert float(result.gwei) == 1_000_000_000.0
        assert result.eth == "1"

    def test_fractional_eth(self) -> None:
        """Test conversion with fractional ETH."""
        result = convert(0.5, "eth")
        assert result.wei == "500000000000000000"
        assert float(result.gwei) == 500_000_000.0
        assert result.eth == "0.5"

    def test_string_input(self) -> None:
        """Test conversion with string input."""
        result = convert("1000", "gwei")
        assert result.wei == "1000000000000"
        assert result.gwei == "1000"

    def test_large_wei(self) -> None:
        """Test conversion with large Wei value."""
        # 1 ETH in Wei
        result = convert("1000000000000000000", "wei")
        assert result.wei == "1000000000000000000"
        assert float(result.gwei) == 1_000_000_000.0
        assert result.eth == "1"

    def test_invalid_unit(self) -> None:
        """Test that invalid unit raises ValueError."""
        with pytest.raises(ValueError, match="Unit must be one of"):
            convert(1, "invalid")  # type: ignore

    def test_zero(self) -> None:
        """Test conversion of zero."""
        result = convert(0, "eth")
        assert result.wei == "0"
        assert result.gwei == "0"
        assert result.eth == "0"

    def test_small_wei(self) -> None:
        """Test conversion of small Wei value."""
        # 1 Wei = smallest unit
        result = convert(1, "wei")
        assert result.wei == "1"
        assert result.eth == "0.000000000000000001"

    def test_precision_preservation(self) -> None:
        """Test that precision is preserved in Wei."""
        # 1.5 Gwei = 1.5 billion Wei
        result = convert("1500000000", "wei")
        assert result.wei == "1500000000"
        assert float(result.gwei) == 1.5


def test_dataclass_str() -> None:
    """Test EthereumValue string representation."""
    value = EthereumValue(wei="1000", gwei="0.000001", eth="0.000000001")
    str_repr = str(value)
    assert "Wei: 1000" in str_repr
    assert "Gwei: 0.000001" in str_repr
    assert "ETH: 0.000000001" in str_repr


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

