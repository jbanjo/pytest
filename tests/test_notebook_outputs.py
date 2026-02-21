from pathlib import Path

def test_output_exists():
    repoRootDirectory = Path(__file__).resolve().parent.parent
    testingDirectory = repoRootDirectory / "notebooks/outputs"
    assert (testingDirectory / "sample_output.txt").exists(), "Sample Output is Missing!"

def test_output_correct(testing_directory, comparison_directory):
    repoRootDirectory = Path(__file__).resolve().parent.parent
    testingDirectory = repoRootDirectory / "notebooks/outputs"
    comparisonDirectory = repoRootDirectory / "tests/comparison_outputs"
    assert (testingDirectory / "sample_output.txt").read_text() == (comparisonDirectory / "sample_output.txt").read_text(), "Sample Output not correct!"