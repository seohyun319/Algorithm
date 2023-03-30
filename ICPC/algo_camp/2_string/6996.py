# bronze1-6996. 애너그램

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    words = list(map(str, input().split()))
    first_word = sorted(list(words[0]))
    second_word = sorted(list(words[1]))
    if first_word == second_word:
        print(words[0], "&", words[1], "are anagrams.")
    else: 
        print(words[0], "&", words[1], "are NOT anagrams.")