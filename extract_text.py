import fitz  # PyMuPDF

# Open the PDF
pdf_path = "/workspace/genderstrat/gen_strat.pdf"  
pdf_document = fitz.open(pdf_path)

# Extract text
text = ""
for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    text += page.get_text()

# Save the extracted text to a file
with open("extracted_text.txt", "w") as text_file:
    text_file.write(text)