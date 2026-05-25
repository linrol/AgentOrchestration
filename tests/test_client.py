import pytest
from src.sdk.client import OrchestratorClient

class TestOrchestratorClient:
    def test_register_agent_invalid_config_type(self):
        client = OrchestratorClient(api_key="test-key")
        with pytest.raises(TypeError, match="config must be a mapping \\(dict\\) or None"):
            client.register_agent("test-agent", "worker", config=[])

        with pytest.raises(TypeError, match="config must be a mapping \\(dict\\) or None"):
            client.register_agent("test-agent", "worker", config="not a dict")
