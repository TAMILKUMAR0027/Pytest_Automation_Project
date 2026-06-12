"""Test suite for verifying application launch / homepage state."""

import pytest

from actions.launch_actions import LaunchActions
from utils.loggerCreator import get_logger

logger = get_logger(__name__)


class TestHome:
    """Smoke tests for the homepage after automatic launch."""

    @pytest.mark.smoke
    @pytest.mark.Prasanna
    def test_homepage_verification(self, driver):
        """Single comprehensive test for homepage. URL is automatically launched by the fixture."""
        drv, _ = driver

        launch_actions = LaunchActions(drv)
        logger.info("Verifying homepage after automatic launch...")

        launch_actions.verify_homepage()