import os
import json
from json_creation import normalize_key, search_key
import re

def clean_values(values):
    cleaned = []
    for v in values:
        s = str(v)
        s = re.sub(r'[^\d.]', '', s)
        if s:
            cleaned.append(round(float(s), 2))
    return cleaned

def iterate_json_files(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                yield json.load(f), filename

def validate_amounts(directory):
    for json_data, filename in iterate_json_files(directory):
        openai_total = clean_values(search_key(normalize_key("Total Gross Pay"), json_data))
        manual_total = clean_values(search_key(normalize_key("Manual Total Gross Pays"), json_data))

        if not openai_total: 
            print(f"❌ Missing OpenAi totals in {filename}.")
        if not manual_total: 
            print(f"❌ Missing Manual totals in {filename}.") 

        if openai_total and manual_total:
            if openai_total != manual_total:
                print(f"❌ OpenAI Total: {openai_total}, Manual Total: {manual_total}; Discrepancy in {filename}")
            else:
                print(f"✅ OpenAI Total: {openai_total}, Manual Total: {manual_total}; {filename}")

# Example usage
if __name__ == "__main__":
    json_folder = "JSONs"
    validate_amounts(json_folder)