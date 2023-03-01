import json
from quantities import 
from jsonschema import validate, ValidationError, FormatChecker

def Validator(target: str):
    print(target + ' CHECK BEGIN')
    with open(target + '/' + target +  '_schema.json', encoding="utf-8") as file_schema:
        json_schema = json.load(file_schema)

    with open(target + '/' + target +  '.json', encoding="utf-8") as file_json:
        json_data = json.load(file_json)
    try:
        validate(json_data, json_schema, format_checker=FormatChecker())
    except ValidationError as e:
        print(e.message)
    print(target + ' CHECK END')

if __name__ == '__main__' :
    Validator("VolumetricFlask")
    Validator("VolumetricPipette")


