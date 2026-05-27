import fitz

def extract_text_from_pdf(pdf_path):

    extracted_text = ""

    try:
        pdf_document = fitz.open(pdf_path)

        for page in pdf_document:
            extracted_text += page.get_text()

        pdf_document.close()

        return extracted_text

    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"