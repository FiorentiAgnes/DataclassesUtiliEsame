import datetime
from dataclasses import dataclass


@dataclass
class Invoice:
    InvoiceId: int
    CustomerId: int
    InvoiceDate: datetime
    BillingAddress: str
    BillingCity: str
    BillingState: str
    BillingCountry: str
    BillingPostalCode: str
    Total: float

    def __hash__(self):
        return hash(self.InvoiceId)

    def __eq__(self, other):
        return self.InvoiceId == other.InvoiceId

    def __str__(self):
        return f"""InvoiceId: {self.InvoiceId}-BillingAddress: {self.BillingAddress}-BillingCity: {self.BillingCity}-BillingPostalCode: {self.BillingPostalCode}-Total: {self.Total}"""