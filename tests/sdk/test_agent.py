import pytest
from src.sdk.agent import BaseAgent

class DummyAgent(BaseAgent):
    async def setup(self):
        pass
    async def handle_task(self, task):
        pass
    async def cleanup(self):
        pass

def test_agent_set_metadata():
    agent = DummyAgent("id", "name")
    agent.set_metadata("key", "value")
    assert agent.get_metadata("key") == "value"

def test_agent_set_metadata_invalid_key():
    agent = DummyAgent("id", "name")
    with pytest.raises(TypeError):
        agent.set_metadata(123, "value")
    with pytest.raises(ValueError):
        agent.set_metadata("", "value")