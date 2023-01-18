from services import thread_service, selenium_service, data_service
from constants import DEFAULT_THREADS, DEFAULT_PAGES
from utils import get_pages


def main():
    threads = int(input(f'Введите количество потоков (default={DEFAULT_THREADS}): ') or DEFAULT_THREADS)
    pages_ = input(f'Введите количество просматриваемых страниц ({DEFAULT_PAGES}, default=all): ') or 'all'

    print('INFO:    ', 'Сбор начальных данных')
    pages, head, data = selenium_service.get_init_data()
    print('INFO:    ', 'Сбор данных')
    pages = get_pages(pages, pages_)
    data += thread_service.run(threads, pages)
    print('INFO:    ', 'Обработка данных')
    data_service.data_processing(head, data)

if __name__ == '__main__':
    main()