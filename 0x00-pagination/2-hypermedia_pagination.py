#!/usr/bin/env python3
'''This is not important
'''
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Help please
        '''
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        self.dataset()
        get_index = __import__('0-simple_helper_function').index_range
        index = get_index(page, page_size)
        return self.__dataset[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Help me pls
        '''
        page_list = self.get_page(page, page_size)
        dataset_len = len(self.__dataset)
        total_pages = dataset_len // page_size
        if dataset_len % page_size != 0:
            total_pages += 1

        get_index = __import__('0-simple_helper_function').index_range
        index = get_index(page, page_size)
        next_page = (page + 1) if len(page_list) == page_size else None
        prev_page = (page - 1) or None
        return {
            'page_size': len(page_list),
            'page': page,
            'data': page_list,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }