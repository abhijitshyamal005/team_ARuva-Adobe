# 🧠 PDF Outline Extractor

This solution extracts structured outlines (document titles and hierarchical headings) from PDF files using PyMuPDF, and outputs the result as a `.json` file for each PDF.

---

## 📁 Project Structure

project-root/
├── Dockerfile
├── app/
│ ├── main.py # PDF processing logic
│ └── requirements.txt # Python dependencies
├── input/ # PDF files to be processed (mounted at /app/input)
├── output/ # Output JSON files (mounted at /app/output)

yaml
Copy
Edit

---

## 🛠️ Build Instructions

Use the following command to build the Docker image:

```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
🚀 Run Instructions
Use the following command to run the solution:

bash
Copy
Edit
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier
⚙️ Expected Behavior
The solution processes all .pdf files inside /app/input.

For each filename.pdf, a corresponding filename.json is created in /app/output.

✅ Output Format
Each .json file will contain the extracted title and a list of outline items:

json
Copy
Edit
{
  "title": "Extracted document title",
  "outline": [
    {
      "level": "H1",
      "text": "Heading text ",
      "page": 0
    },
    {
      "level": "H2",
      "text": "Subheading text ",
      "page": 1
    }
  ]
}
The text values are trimmed and suffixed with a space for formatting consistency.

📦 Dependencies
This project uses a single Python package:

text
Copy
Edit
PyMuPDF==1.23.3
Defined in app/requirements.txt.

🔐 Security & Isolation
Runs in Docker with no external network access (--network none)

All input/output file operations are sandboxed via mounted volumes

💡 Notes
Heading levels are detected using regex patterns and common keywords.

The title is extracted from the topmost, largest text near the top center of the first page.

Duplicate headings are filtered.