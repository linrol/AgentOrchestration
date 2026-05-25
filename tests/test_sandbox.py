import pytest
from src.agent.sandbox import ResourceLimits

def test_resource_limits_rejects_disk_mb():
    with pytest.raises(ValueError, match="disk_mb limit is not currently supported"):
        ResourceLimits(disk_mb=100)

def test_resource_limits_allows_no_disk_mb():
    limits = ResourceLimits()
    assert limits.disk_mb is None

