import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using PyPDF2.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""  # Handles pages with no text
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

if __name__ == "__main__":
    # Replace 'sample.pdf' with the path to your PDF file
    pdf_file = 'sample.pdf'
    extracted_text = extract_text_from_pdf(pdf_file)

    if extracted_text:
        print("Extracted Text:\n")
        print(extracted_text)
    else:
        print("No text found in the PDF.")
