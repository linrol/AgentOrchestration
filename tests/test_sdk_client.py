import pytest
from src.sdk.client import OrchestratorClient

def test_register_agent_blank_name():
    client = OrchestratorClient(base_url="http://test.local", api_key="test_key")
    
    with pytest.raises(ValueError, match="Agent name cannot be blank"):
        client.register_agent("", "worker")
        
    with pytest.raises(ValueError, match="Agent name cannot be blank"):
        client.register_agent("   ", "worker")
