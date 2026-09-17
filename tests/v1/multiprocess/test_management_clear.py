# SPDX-License-Identifier: Apache-2.0
"""Tests for multiprocess management cache clearing."""

# Standard
from unittest.mock import MagicMock

# First Party
from lmcache.v1.multiprocess.modules.management import ManagementModule


def test_management_clear_preserves_locked_objects() -> None:
    """Management CLEAR uses non-forced storage clear with memchecks."""
    ctx = MagicMock(name="server_context")
    management = ManagementModule(ctx)

    assert management.clear() is None

    ctx.storage_manager.memcheck.assert_called()
    assert ctx.storage_manager.memcheck.call_count == 2
    ctx.storage_manager.clear.assert_called_once_with(force=False)
