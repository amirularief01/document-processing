# Apache Tika Document Parser and Word Document Generator

## Overview

This project is a Python-based tool that extracts text from multiple documents using Apache Tika and compiles the extracted data into a single Microsoft Word document. The tool processes files in a specified folder, identifies headers and content from the documents, and organizes the output into a structured two-column table.

## Features

- Supports multiple document types: `.pdf`, `.pptx`, `.docx`, `.txt`
- Extracts headers and corresponding content from documents
- Consolidates all extracted data into a single Word document
- Dynamically handles errors and skips unsupported or unparseable files
- Logs processing progress for transparency

## Requirements

- Python 3.7 or higher
- Apache Tika library
- python-docx library

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install tika python-docx
   ```
3. Ensure Apache Tika is properly installed and configured. Follow the [official Tika documentation](https://tika.apache.org/) if needed.

## Usage

1. Place all the documents you want to process in a folder.
2. Modify the script to specify the folder path and output file name:
   ```python
   input_folder = "path_to_your_folder"  # Replace with your folder path
   output_file = "Extracted_Table.docx"  # Output Word file name
   ```
3. Run the script:
   ```bash
   python tika_word_parser.py
   ```
4. The extracted data will be saved in the specified Word document.

## Example

### Input Folder

The folder contains the following files:

- `document1.pdf`
- `presentation.pptx`
- `notes.txt`

### Output Word Document

The Word file, `Extracted_Table.docx`, will have the following structure:

| Header            | Content                          |
| ----------------- | -------------------------------- |
| Document Header 1 | Extracted content from document1 |
| Document Header 2 | Extracted content from document2 |

## Limitations

- Header and content extraction relies on simple logic and may not work for all document structures.
- Large files may take longer to process.

## Future Enhancements

- Add support for additional file formats.
- Improve the logic for detecting headers and content for complex documents.
- Provide a GUI for easier file selection and processing.

## Contributing

If you want to contribute to this project, feel free to submit a pull request or raise an issue in the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

