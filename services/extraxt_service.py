import re

def extract_abstract_from_first_page(text):
    """Extract abstract based on known structure."""
    text = text.replace('\n', ' ').strip()
    match = re.search(r'(?i)abstract(.*?)(?=(\d{0,2}\.?\s?introduction|1\s?introduction|I\.\s?Introduction|Background))', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def clean_body_text(full_text):
    """Remove abstract and references."""
    # Remove the abstract section (if found)
    full_text = re.sub(r'(?i)^abstract.*?(?=(\d{0,2}\.?\s?introduction|1\s?introduction|I\.\s?Introduction|Background))', '', full_text, flags=re.DOTALL)
    
    # Cut before references/bibliography
    full_text = re.split(r'(?i)(references|bibliography)', full_text)[0]
    
    return full_text.strip()
