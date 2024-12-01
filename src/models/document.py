from datetime import date
from dataclasses import dataclass, field

@dataclass
class Document:
    document_no: str = ''
    reference_no: str = ''
    container_no: str = ''
    invoice_no: str = ''

    container_type: str = ''
    packages: str = ''

    document_date: date = None

    released: list[str] = field(default_factory=list)
    transferred: list[str] = field(default_factory=list)
    approved: list[str] = field(default_factory=list)