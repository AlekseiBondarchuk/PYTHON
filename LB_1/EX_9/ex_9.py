num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

  def lastElem(list, elem):
    return len(list)-1-list[::-1].index(elem)
  
print(lastElem(num_list,10), ' ', lastElem(word_list,'python'))
