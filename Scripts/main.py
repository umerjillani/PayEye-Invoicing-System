# total of all entities is not being fetched in json 
# fetch / calculate total of all gross pays 

from ocr import perform_OCR
from json_creation import create_JSON
from json_creation import REQUIRED_KEYS
from validator import validate_amounts
from pathlib import Path


if __name__ == "__main__":
    input_folder = Path("Data") # excel, Images, txt files
    output_folder = Path("OCR_Output") # OCR output folder 
    output_folder.mkdir(parents=True, exist_ok=True)  
    json_folder = Path("JSONs") # JSON output folder
    json_folder.mkdir(parents=True, exist_ok=True)
    
    perform_OCR(input_folder, output_folder)  
    create_JSON(output_folder, REQUIRED_KEYS, json_folder)
    validate_amounts(json_folder) 
