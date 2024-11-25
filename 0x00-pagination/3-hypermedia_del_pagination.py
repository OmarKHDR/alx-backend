#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''This is that
        '''
        self.indexed_dataset()
        curr_index = index
        next_index = curr_index + page_size
        assert curr_index < len(self.__indexed_dataset)
        new_size = 0
        data = list(self.__indexed_dataset.values())[curr_index:next_index]
        # for i in range(curr_index, next_index):
        #     if i in self.__indexed_dataset:
        #         data.append(self.__indexed_dataset[i])
        #         new_size += 1
        return {
            'index': curr_index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
        }
