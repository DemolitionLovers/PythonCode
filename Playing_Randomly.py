#!/usr/bin/env python3
import time
import random


# This was my first commit <3


def rand_string():
  char_list = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g',
      'h', 'i', 'j', 'k', 'l', 'm', 'n',
      'o', 'p', 'q', 'r', 's', 't', 'u',
      'v', 'w', 'x', 'y', 'z',

      'A', 'B', 'C', 'D', 'E', 'F', 'G',
      'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U',
      'V', 'W', 'X', 'Y', 'Z',

      '1', '2', '3', '4', '5',
      '6', '7', '8', '9', '0',

      '!', '"', '£', '$', '%', '^',
      '&', '*', '(', ')', '_', '+',
      '[', ']', ';', '\'', '#',
      ',', '.', '/', '\\', '`',
      '{', '}', ':', '@', '~',
      '<', '>', '?', '|', '¬',
    ]

  to_print = random.choice(char_list) + random.choice(char_list)

  for i in range(26):
    to_print = to_print + random.choice(char_list)

  return to_print


def main():
  while True:
    for i in range(10):
      print(rand_string())
    time.sleep(0.1)


if __name__ == '__main__':
  main()
