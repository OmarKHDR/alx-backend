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
        assert page > 0
        assert page_size > 0
        get_index = __import__('0-simple_helper_function').get_index
        index = get_index(page, page_size)
        return self.__dataset[index[0]:index[1]]
