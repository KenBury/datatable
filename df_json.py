import json
import pandas as pd

def df_to_json_indented(df, indent=4):
    """
    Converts a Pandas DataFrame to a JSON string with indentation.

    Args:
        df: The Pandas DataFrame to convert.
        indent: The number of spaces to indent.

    Returns:
        A JSON string with the specified indentation.
    """

    json_str = df.to_json(orient='records')
    json_obj = json.loads(json_str)
    formatted_json = json.dumps(json_obj, indent=indent)
    return formatted_json

# Example usage:
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
indented_json = df_to_json_indented(df, indent=4)
print(indented_json)
