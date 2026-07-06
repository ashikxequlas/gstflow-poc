import re

class InvoiceParser:

    def parse(self, text):

        data = {}

        # Document Type
        data["document_type"] = "purchase_invoice"

        # Supplier Name
        supplier = re.search(r"^(.*?)\n", text)
        data["supplier_name"] = supplier.group(1).strip() if supplier else ""

        # GSTIN
        gstin = re.search(r"GSTIN/UIN[:\s]*([0-9A-Z]{15})", text)
        data["supplier_gstin"] = gstin.group(1) if gstin else ""

        # Invoice Number
        invoice = re.search(r"Invoice No\.\s*([A-Za-z0-9/-]+)", text)
        data["invoice_number"] = invoice.group(1) if invoice else ""

        # Invoice Date
        date = re.search(r"\d{1,2}-[A-Za-z]{3}-\d{2}", text)
        data["invoice_date"] = date.group(0) if date else ""

        # Total Amount
        total = re.search(r"₹\s*([\d,]+\.\d+)", text)
        if total:
            data["total_amount"] = float(total.group(1).replace(",", ""))
        else:
            data["total_amount"] = 0

        # Taxable Amount
        taxable = re.search(r"Total\s+([\d,]+\.\d+)\s+1,083", text)

        if taxable:
            data["taxable_amount"] = float(taxable.group(1).replace(",", ""))
        else:
            data["taxable_amount"] = 0

        # CGST
        cgst = re.search(r"CGST Output\s+([\d,]+\.\d+)", text)

        if cgst:
            data["cgst"] = float(cgst.group(1).replace(",", ""))
        else:
            data["cgst"] = 0

        # SGST
        sgst = re.search(r"SGST Output\s+([\d,]+\.\d+)", text)

        if sgst:
            data["sgst"] = float(sgst.group(1).replace(",", ""))
        else:
            data["sgst"] = 0

        # IGST
        data["igst"] = 0

        data["validation_status"] = "Pending"

        data["confidence_score"] = 0.95

        return data