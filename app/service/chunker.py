def chunk_text(text:str,chunk_size = 500,overlaps = 100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlaps

    return chunks