"""
Test all active deployments!!!

"""
import pytest

from autoscab.deployments.deployment import Deployment

@pytest.fixture(scope="function", params=Deployment.get_deployments(active=True).values())
def active_deployments(request):
    deploy = request.param
    yield deploy



def test_deployments(active_deployments):
    postbot = active_deployments.make()
    result = postbot.apply()
    assert result == True