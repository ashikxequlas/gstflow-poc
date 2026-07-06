from ocr_service import OCRService
from parser import InvoiceParser
from gst_validator import GSTValidator
from storage import Storage

ocr = OCRService()
parser = InvoiceParser()
validator = GSTValidator()
storage = Storage()

invoice_path = "../sample_invoices/invoice_1.pdf"

pages = ocr.extract_text(invoice_path)

all_invoices = []

for i, page_text in enumerate(pages):

    print(f"\nProcessing Invoice {i+1}")

    if page_text.strip() == "":
        continue

    invoice = parser.parse(page_text)

    invoice = validator.validate(invoice)

    all_invoices.append(invoice)

print(f"\nTotal Invoices Extracted : {len(all_invoices)}")

storage.save_json(all_invoices)

storage.save_csv(all_invoices)