class InvoiceSchema:

    @staticmethod
    def empty_invoice():
        return {
            "document_type": "purchase_invoice",
            "supplier_name": "",
            "supplier_gstin": "",
            "invoice_number": "",
            "invoice_date": "",
            "taxable_amount": 0.0,
            "cgst": 0.0,
            "sgst": 0.0,
            "igst": 0.0,
            "total_amount": 0.0,
            "validation_status": "Pending",
            "confidence_score": 0.0
        }