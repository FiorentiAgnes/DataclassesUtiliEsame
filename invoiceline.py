from dataclasses import dataclass


@dataclass
class InvoiceLine:
    InvoiceLineId: int
    InvoiceId: int
    TrackId: int
    UnitPrice: float
    Quantity: int

    def __hash__(self):
        return hash(self.InvoiceLineId)
    def __eq__(self, other):
        return self.InvoiceLineId == other.InvoiceLineId
    def __str__(self):
        return f"""InvoiceLineId: {self.InvoiceLineId} UnitPrice: {self.UnitPrice} Quantity: {self.Quantity}"""
