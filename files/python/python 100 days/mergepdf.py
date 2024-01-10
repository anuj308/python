from pypdf import PdfReader

reader = PdfReader("2000.txt")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()