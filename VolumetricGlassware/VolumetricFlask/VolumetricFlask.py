import json
from jsonschema import validate, ValidationError, FormatChecker

with open('VolumetricFlask/VolumetricFlask_schema.json', encoding="utf-8") as file_schema:
    json_schema = json.load(file_schema)

with open('VolumetricFlask/VolumetricFlask.json', encoding="utf-8") as file_json:
    json_data = json.load(file_json)

try:
    validate(json_data, json_schema, format_checker=FormatChecker())
except ValidationError as e:
    print(e.message)

print('CHECK END')