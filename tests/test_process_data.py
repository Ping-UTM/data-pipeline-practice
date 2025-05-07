import pandas as pd
from scripts.process_data import remove_duplicates

def test_remove_duplicates(tmp_path):
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Alice"],
        "age": [25, 30, 25]
    })
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    df.to_csv(input_file, index=False)

    remove_duplicates(input_file, output_file)

    result = pd.read_csv(output_file)
    assert len(result) == 2
