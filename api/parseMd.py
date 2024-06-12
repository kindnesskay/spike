import os
import json

def md_to_json(md_content):
    # Initialize an empty dictionary to hold the parsed content
    result = {}
    current_section = None
    
    lines = md_content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('**') and line.endswith('**'):
            # This is a new section
            current_section = line.strip('**').strip()
            result[current_section] = []
        elif line.startswith('* '):
            # This is a list item
            if current_section:
                result[current_section].append(line[2:])
        elif line:
            # This is a regular line (part of the current section)
            if current_section:
                if isinstance(result[current_section], list):
                    result[current_section] = ' '.join(result[current_section])
                result[current_section] += ' ' + line
            else:
                current_section = 'General'
                result[current_section] = line
    
    # Convert any remaining list sections to single string if they were actually descriptions
    for key, value in result.items():
        if isinstance(value, list) and len(value) == 1:
            result[key] = value[0]
    
    return result

def read_md_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def write_json_file(data, output_path):
    try:
        with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"JSON content has been written to '{output_path}'")
    except Exception as e:
        print(f"An error occurred while writing the JSON file: {e}")

# Example usage
md_file_path = 'files/file/readme.md'  # Replace with your actual file path
json_output_path = 'output.json'  # Replace with your desired output file path

md_content = read_md_file("./files/cd6b555a796d4fd89ff18bd92f8fc6c0/README.md")
if md_content:
    json_data = md_to_json(md_content)
    write_json_file(json_data, json_output_path)

