import json
from datetime import datetime
from app.processor import process_documents

if __name__ == "__main__":
    with open("inputs/input.json", "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = process_documents(input_data)

    # Add timestamp
    result["metadata"]["processing_timestamp"] = datetime.now().isoformat()

    # Write to output
    with open("output/challenge1b_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
