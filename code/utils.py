from pathlib import Path

def get_or_create_path(path, subpath):
    """Возвращает или создает путь"""
    filepath = Path(path / subpath)
    filepath.mkdir(parents=True, exist_ok=True)
    return filepath

def get_pages(pages, input_pages):
    if input_pages != 'all':
        input_pages = int(input_pages)
        if input_pages < pages:
            pages = input_pages
    return pages