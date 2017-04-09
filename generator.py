#!/usr/bin/python
import itertools
from collections import Counter

keywords=input("Keywords about victim (Split with ','): ")
words=keywords.split(",")

contain_number=input("Words contains numbers('95','2017','123')? [y/N]: ")
if(contain_number == "Y" or contain_number =="y"):
    numbers_entered=input("Numbers about victim (Split with ','): ")
    numbers=numbers_entered.split(",")

rule_punctuation=input("Words contains punctuation('.',',','_')? [y/N]: ")
pointings=""
if(rule_punctuation == "Y" or rule_punctuation =="y"):
    rule_pointings=input("Words contains these punctuations (Split with blank. Ex: '. , _'): ")
    pointings=rule_pointings.split(" ")

length_words=len(words)
length_numbers=len(numbers)
length_pointings=len(pointings)

#Words lists for informatin about how many words contain
words_lists=[]
words_lists_with_number=[]
complex_words=[]
complex_words_removed=[]
#Contain a just word, contain two words, contain three...
for counter in range(0,length_words):
    words_lists.append([])

for counter in range(0,length_words):
    words_lists_with_number.append([])

#Informations
print("Words:{}\nPunctuation:{}\nNumbers:{}".format(length_words,length_pointings,length_numbers))


def generate_word(words, min, max):

    for i in range(int(min), int(max)+1):
        for j in itertools.product(words, repeat=i):
            #create a list and add items to this list
            #count same words in list, if a word repeats more 2 times, delete. I guess anybody don't repeat a word more 2 times.
            counter_for_join_word=len(j)
            #print(counter_for_join_word)
            counter_list = Counter(j)
            print(counter_list)
            for element in j:
                if (counter_list[element]<3):
                    #Add every produced words to list for how many words contains?
                    if not ''.join(j) in words_lists[counter_for_join_word-1]:
                        words_lists[counter_for_join_word-1].append(''.join(j))
                        #yield ''.join(j)
                        add_numbers(''.join(j),counter_for_join_word-1)

                    #add pointings to one word
                    if(length_pointings>0 and len(j)==1):
                        for mark in pointings:
                            #add to end
                            if not j[0]+mark in words_lists[0]:
                                words_lists[0].append(j[0]+mark)
                                #yield j[0]+mark
                                add_numbers(j[0]+mark,0)
                            #add to head
                            if not mark+j[0] in words_lists[0]:
                                words_lists[0].append(mark+j[0])
                                #yield mark+j[0]
                                add_numbers(mark+j[0],0)


                    if(length_pointings>0 and len(j)>1):
                        for mark in pointings:
                            if not mark.join(j) in words_lists[counter_for_join_word-1]:
                                words_lists[counter_for_join_word-1].append(mark.join(j))
                                #yield mark.join(j)
                                add_numbers(mark.join(j),counter_for_join_word-1)

def add_numbers(word_for_add, howmanywords):
    #print(word_for_add,howmanywords)
    for number in numbers:
        #add to end
        if not number+word_for_add in words_lists[howmanywords]:
            words_lists_with_number[howmanywords].append(number+word_for_add)
            #print(number+word_for_add)
        #add to head
        if not word_for_add+number in words_lists[howmanywords]:
            words_lists_with_number[howmanywords].append(word_for_add+number)
            #print(word_for_add+number)

#this function generate keywords more complex but not best.
def generate_complex():
    for words_list in words_lists:
        for word in words_list:
            for words_list_with_number in words_lists_with_number:
                for word_with_number in words_list_with_number:
                    complex_words.append(word+word_with_number)

    for complex_word in complex_words:
        for word_to_count in words:
            if(complex_word.count(word_to_count)>1):
                try:
                    #print(word_to_count, complex_word, complex_word.count(word_to_count))
                    complex_words_removed.append(complex_word)
                except:
                    pass

    complex_words_finally=list(set(complex_words).difference(complex_words_removed))
    print(complex_words_finally)

generate_word(words, 1, length_words)

#print("\n",counter_words," words generated.\n")
print(words_lists)
print(words_lists_with_number)

generate_complex()
