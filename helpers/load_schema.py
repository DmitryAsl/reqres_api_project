import os
import json


def load_schema(schema_name):
    schema_path = os.path.join(os.path.dirname(__file__), '../data/json_schemas', schema_name + '.json')
    with open(schema_path) as f:
        return json.load(f)
