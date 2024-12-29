import os
import time
from extract_text import extract_text_from_pdf, extract_text_from_pptx, extract_text_with_tika
from process_text import process_text_with_groq
from create_document import create_word_document

def main(input_folder, output_file):
    # Collect all files in the input folder
    files = [f for f in os.listdir(input_folder) if f.endswith(('.pdf', '.pptx'))]
    headers_and_content = {}

    # Process files one by one
    for filename in files:
        file_path = os.path.join(input_folder, filename)

        # Extract text from the file
        text = extract_text_with_tika(file_path)
        # Process text with Groq
        processed_text = process_text_with_groq(text)

        # Assuming Groq output is structured as "Header: Content"
        for line in processed_text.split("\n"):
            if ":" in line:
                header, content = line.split(":", 1)
                headers_and_content[header.strip()] = content.strip()

        # Append the current file's processed data to the output document
        create_word_document(headers_and_content, output_file)
        headers_and_content.clear()  # Clear the content after saving to avoid duplication

        # Rate limiting: wait for 60 seconds after each file
        print(f"Processed file: {filename}. Waiting for 1 minute before processing the next file...")
        time.sleep(60)

    print(f"All documents processed. Final output saved to {output_file}")

if __name__ == "__main__":
    input_folder = r"C:\Users\amiru\Documents\Self Project\notes-processing\documents"  # Replace with your folder path
    output_file = "output.docx"  # The output Word document
    main(input_folder, output_file)

