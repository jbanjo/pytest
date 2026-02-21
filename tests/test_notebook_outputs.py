def test_output_exists(testing_directory):
    assert (testing_directory / "sample_output.txt").exists(), "Sample Output is Missing!"

def test_output_correct(testing_directory, comparison_directory):
    assert (testing_directory / "sample_output.txt").read_text() == (comparison_directory / "sample_output.txt").read_text(), "Sample Output not correct!"