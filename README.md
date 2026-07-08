# GSTFlow POC - GST Invoice OCR Processing

## Project Overview

GSTFlow POC is a proof-of-concept project that automates GST invoice processing using OCR (Optical Character Recognition).

The system extracts important information from GST invoices and converts it into structured JSON and CSV formats.

## Problem Statement

Companies receive a large number of GST invoices from suppliers.

Traditionally, accountants manually read invoices and enter data into accounting systems, which is:

- Time-consuming
- Error-prone
- Difficult to scale

This project automates the extraction process using OCR technology.

---

## Features

- Extract text from PDF invoices
- Support image invoices (JPG, PNG)
- OCR using Tesseract
- Extract GST fields using Regex
- Validate extracted information
- Export results to JSON
- Export results to CSV

---

## Project Structure

```text
gstflow-poc/
│
├── backend/
│   ├── main.py
│   ├── ocr_service.py
│   ├── parser.py
│   ├── gst_validator.py
│   ├── storage.py
│   └── schemas.py
│
├── sample_invoices/
│
├── outputs/
│   ├── extracted_invoices.json
│   └── extracted_invoices.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

GST Invoice

↓

OCR / PDF Text Extraction

↓

Text Extraction

↓

Field Parsing

↓

GST Validation

↓

JSON Output

↓

CSV Output

---

## Technologies Used

- Python
- Tesseract OCR
- pdfplumber
- pdf2image
- Pillow
- Regular Expressions (Regex)
- JSON
- CSV
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd gstflow-poc
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Move to backend folder:

```bash
cd backend
```

Run:

```bash
python main.py
```

---

## Sample Output

### JSON

```json
{
  "document_type": "purchase_invoice",
  "supplier_name": "ABC Traders",
  "supplier_gstin": "29ABCDE1234F1Z5",
  "invoice_number": "INV-1024",
  "invoice_date": "2026-07-01",
  "taxable_amount": 10000,
  "cgst": 900,
  "sgst": 900,
  "igst": 0,
  "total_amount": 11800,
  "validation_status": "passed",
  "confidence_score": 0.91
}
```

### CSV

| Supplier | GSTIN | Invoice Number | Total Amount |
|----------|-------|---------------|-------------|
| ABC Traders | 29ABCDE1234F1Z5 | INV-1024 | 11800 |

---

## Current Limitations

- Supports limited invoice layouts.
- Complex tables may require additional parsing logic.
- Handwritten invoices are not supported.

---

## Future Improvements

- Support multiple invoice templates.
- Use AI-based OCR models.
- Add web dashboard.
- Integrate with accounting software.
- Add GST portal integration.

---

## Author

Internship Project - GSTFlow OCR POC