#1 and 2a and then 3,4, or 5
import os

def reverse(filename):
    file = open(filename, 'r')
    text = file.read()
    words = text.split("\n")
    for i in range(len(words)):
        words[i] = words[i][::-1]
    words = str(words)
    file_two = open('output.txt', "w")
    file_two.write(words)
    file.close()

#reverse('connectives.txt')

def file_sum(filename):
    sum = 0
    file = open(filename, 'r')
    file_two = open('output2.txt', "w")
    text = file.read()
    words = text.split("\n")
    for i in range(len(words)):
        if words[i].isdigit():
            sum += int(words[i])
        else:
            file_two.write(words[i] + "\n")
    print(sum)
    file.close()

#file_sum(('connectives.txt'))

def containing_word(filename):
    sentence_start = 0
    sentence_end = 0
    Begin = False
    multiple = False
    file = open(filename, 'r')
    file_two = open('output3.txt', "w")
    text = file.read()
    words = text.split(" ")
    for i in range(len(words)):
        if words[i][-1] == ".":
            if Begin == False:
                sentence_end = i
                Begin = True
            else:
                sentence_start = i
                Begin = False
                multiple = False
        if words[i] == "the":
            words[i] = "THE"
            multiple = True
            for x in range(sentence_end - sentence_start, sentence_start):
                file_two.write(words[x] + " ")
    file.close()

containing_word('sentences.txt')