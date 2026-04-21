"""Tests for exchange_registers/register_exmo.py."""

from __future__ import annotations

from bt_api_exmo.registry_registration import register_exmo


class TestRegisterExmo:
    """Tests for EXMO registration module."""

    def test_module_imports(self):
        """Test module can be imported."""
        assert register_exmo is not None
