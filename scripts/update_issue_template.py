import yaml
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Update the options of a dropdown in a YAML file.')
parser.add_argument('file', help='The path to the YAML file.')
parser.add_argument('dropdown_name', help='The dropdown name to bind the options.')
parser.add_argument('options', help='The new options to replace the existing ones, separated by a special character.')

args = parser.parse_args()

# Split the options string into a list of options
options = args.options.split('|')

# Open the file and load the content
with open(args.file, 'r') as file:
    content = yaml.safe_load(file)

# Traverse the body list to find the dropdown and replace the options
for item in content['body']:
    if isinstance(item, dict) and item.get('id') == args.dropdown_name:
        item['attributes']['options'] = options

# Write the updated content back to the file
with open(args.file, 'w') as file:
    yaml.safe_dump(content, file, sort_keys=False)

# Print the updated content
print(yaml.dump(content, sort_keys=False))
