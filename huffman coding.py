import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(data):
    frequency_table = defaultdict(int)
    for char in data:
        frequency_table[char] += 1
    return frequency_table


def build_huffman_tree(frequency_table):
    priority_queue = []
    for char, freq in frequency_table.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(priority_queue, node)

    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(priority_queue, merged_node)

    return heapq.heappop(priority_queue)


def build_encoding_table(root):
    encoding_table = {}

    def traverse(node, code):
        if node.char is not None:
            encoding_table[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(root, "")

    return encoding_table


def huffman_encode(data):
    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)
    encoded_data = "".join(encoding_table[char] for char in data)

    return encoded_data, huffman_tree


def huffman_decode(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = huffman_tree

    return decoded_data


# Example usage:
data = "hello world"
encoded_data, huffman_tree = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, huffman_tree)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
