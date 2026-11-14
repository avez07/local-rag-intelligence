from pypdf import PdfReader
from pathlib import Path


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == '.pdf':
        reader  =  PdfReader(file_path)
        print("PDF pages:", len(reader.pages))

        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

        print("Extracted characters:", len(text))
        return text

    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")

    raise ValueError("Unsupport file format")
