#
# def chars_from_string(string):
#     chars = dict()
#     for i in range(len(string)):
#         chars.setdefault(string[i], []).append(i)
#     return chars
#
# def find_beg_str_char_also_in_end_str(beg_str, end_str_chars, i=0):
#     i = 0
#     while i != len(beg_str):
#         if beg_str[i] not in end_str_chars:
#             i += 1
#     return i
#
# def find_palindromes(strings):
#     n = len(strings)
#     beg_str = strings[0]
#     end_str = strings[-1]
#     beg_str_chars = chars_from_string(beg_str)
#     end_str_chars = chars_from_string(end_str)
#     # need a function that takes i, j, i an index into beg_str
#     # j and index into end_str such that
#     # beg_str, end_str, i, j will give me a set of pairs
#     # that when put together make a palindrome
#
#     # j = -1
#
#     current_pairs = set()
#     # while
#
# from itertools import product
#
# class Subseq(object):
#     """ will use ss in client code as vairable name """
#     def __init__(self, string_index, subseq_start, subseq_end):
#         self.string_index = string_index
#         self.subseq_start = subseq_start
#         self.subseq_end = subseq_end
#
# def find_pairs_from_2_strings(beg_str, end_str, beg_str_chars, end_str_chars, i, j):
#     # i = find_beg_str_char_also_in_end_str(beg_str, end_str_chars, i=0)
#     # places_to_explore_in_end_str = end_str_chars[beg_str[i]]
#
#     # pairs = set()
#     index_pair = []
#     for c in beg_str_chars:
#         if c in end_str_chars:
#             index_pair.extend([x for x in product(beg_str_chars[c], end_str_chars[c])])
#             # pairs.add(index_pair)
#     num_pairs = len(index_pair)
#     for i, j in index_pair:
#         while i+1 < len(beg_str) and j-1 >= 0:
#             i+=1
#             j-=1
#
#                 num_pairs += 1
#     return num_pairs
#
# def test_find_pairs_from_2_strings_1():
#     beg_str = 'aa'
#     end_str = 'aa'
#     beg_str_chars = chars_from_string(beg_str)
#     end_str_chars = chars_from_string(end_str)
#     num_pairs = find_pairs_from_2_strings(beg_str, end_str, beg_str_chars,
#                                       end_str_chars, i=0, j=-1)
#     assert num_pairs == 5
#
# def test_find_pairs_from_2_strings_2():
#     beg_str = 'abc'
#     end_str = 'abc'
#     beg_str_chars = chars_from_string(beg_str)
#     end_str_chars = chars_from_string(end_str)
#     num_pairs = find_pairs_from_2_strings(beg_str, end_str, beg_str_chars,
#                                       end_str_chars, i=0, j=-1)
#     print num_pairs
#
# def test3():
#     strings = ['abd','blababla']
#     print find_palindromes(strings)
#
#
# if __name__ == '__main__':
#     test_find_pairs_from_2_strings_1()
#     test_find_pairs_from_2_strings_2()
