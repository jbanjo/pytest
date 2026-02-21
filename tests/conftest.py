from pathlib import Path
import shutil
import pytest
import os

repoRootDirectory = Path(os.getcwd()).resolve().parent
testingDirectory = repoRootDirectory / "notebooks/outputs"
comparisonDirectory = repoRootDirectory / "tests/comparison_outputs"

def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    testingDirectory.mkdir(exist_ok=True)

def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    shutil.rmtree(testingDirectory)

@pytest.fixture
def testing_directory():
    return testingDirectory

@pytest.fixture
def comparison_directory():
    return comparisonDirectory