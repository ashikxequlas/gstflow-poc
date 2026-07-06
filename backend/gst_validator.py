class GSTValidator:

    def validate(self, invoice_data):

        errors = []

        # Supplier Name
        if not invoice_data.get("supplier_name"):
            errors.append("Supplier Name Missing")

        # GSTIN
        gstin = invoice_data.get("supplier_gstin", "")

        if len(gstin) != 15:
            errors.append("Invalid GSTIN")

        # Invoice Number
        if not invoice_data.get("invoice_number"):
            errors.append("Invoice Number Missing")

        # Invoice Date
        if not invoice_data.get("invoice_date"):
            errors.append("Invoice Date Missing")

        # Total Amount
        if invoice_data.get("total_amount", 0) <= 0:
            errors.append("Invalid Total Amount")

        # Final Status
        if len(errors) == 0:
            invoice_data["validation_status"] = "Passed"
        else:
            invoice_data["validation_status"] = "Failed"

        invoice_data["validation_errors"] = errors

        return invoice_data