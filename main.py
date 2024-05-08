def main():
  with open('books/frankenstein.txt', 'r') as f:
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = character_count(text)
    dict_list = create_dictionary_list(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for d in dict_list:
      print(f"The '{d['letter']}' character was found {d['count']} times")
    print(f"--- End report ---")


def get_word_count(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def character_count(text):
  count = {}
  for char in text:
    char_lower = char.lower()
    if char_lower.isalpha():
      if char_lower in count:
        count[char_lower] += 1
      else:
        count[char_lower] = 1
  return count

def create_dictionary_list(dictionary):
  dictionary_list = [{'letter': key, 'count': value} for key, value in dictionary.items()]
  dictionary_list.sort(key=lambda item: item['count'], reverse=True)
  return dictionary_list

if __name__ == '__main__':
  main()