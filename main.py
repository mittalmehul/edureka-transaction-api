from swagger_parser import SwaggerParser

swagger_path = input("Enter swagger file path: ")
parser = SwaggerParser(swagger_path=swagger_path)  # Init with file

# Get an example of dict for the definition Foo
paths = list(parser.paths.keys())
print(paths)