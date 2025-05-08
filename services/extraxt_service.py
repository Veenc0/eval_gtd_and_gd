import re

def extract_abstract_from_first_page(text):
    """Extract abstract based on known structure."""
    text = text.replace('\n', ' ').strip()
    match = re.search(r'(?i)abstract(.*?)(?=(\d{0,2}\.?\s?introduction|1\s?introduction|I\.\s?Introduction|Background))', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def clean_body_text(full_text):
    full_text = re.sub(
        r'(?i)abstract\s*[:-]?\s*.*?(?=keywords|introduction|1\s?introduction|background)',
        '',
        full_text,
        flags=re.DOTALL
    )
    full_text = re.split(r'(?i)\b(references|bibliography)\b', full_text)[0]
    return full_text.strip()

