# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 07:36:55 2023

@author: Andre
"""

import heapq
import csv
import json
from collections import defaultdict

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(symbol_freq):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in symbol_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node.symbol is not None:
        huffman_codes[str(node.symbol)] = current_code
    if node.left is not None:
        build_huffman_codes(node.left, current_code + '0', huffman_codes)
    if node.right is not None:
        build_huffman_codes(node.right, current_code + '1', huffman_codes)

def huffman_compress_csv(input_file, compressed_data_file, huffman_dict_file):
    symbol_freq = defaultdict(int)

    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for symbol in row:
                symbol_freq[symbol] += 1

    root = build_huffman_tree(symbol_freq)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    with open(compressed_data_file, 'w') as compressed_file:
        with open(input_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                row_data = [huffman_codes[symbol] for symbol in row]
                compressed_file.write(','.join(row_data) + '\n')

    with open(huffman_dict_file, 'w') as dict_file:
        json.dump(huffman_codes, dict_file)

"""if __name__ == "__main__":
    input_file = "datos.csv"
    compressed_data_file = "compressed_data.csv"
    huffman_dict_file = "huffman_dict.json"
    huffman_compress_csv(input_file, compressed_data_file, huffman_dict_file)"""





