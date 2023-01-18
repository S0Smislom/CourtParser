import pandas as pd
from datetime import datetime

from .file_service import write_file

def data_processing(head, data):
    """Обрабатывает и записывает данные в файл"""
    print('INFO:    ', 'Подготовка данных')
    df = pd.DataFrame(data, columns=head)
    filename = datetime.now().strftime("%m.%d.%Y")
    write_file(filename, df)
    return filename
