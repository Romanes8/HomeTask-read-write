
with open('Task3 files/1.txt', encoding='utf8') as f:
    count = 0
    for i in f:
        count+=1
        length_read1 = count

with open('Task3 files/1.txt', encoding='utf8') as f:
    read1 = f.read()

with open('Task3 files/2.txt', encoding='utf8') as f:
    count = 0
    for i in f:
        count+=1
        length_read2 = count

with open('Task3 files/2.txt', encoding='utf8') as f:
    read2 = f.read()

with open('Task3 files/3.txt', encoding='utf8') as f:
    count = 0
    for i in f:
        count+=1
        length_read3 = count

with open('Task3 files/3.txt', encoding='utf8') as f:
    read3 = f.read()

list_fileNames = ['1.txt', '2.txt', '3.txt']
list_length = [length_read1, length_read2, length_read3]
list_read = [read1, read2, read3]
zipped_list = sorted(zip(list_length, list_read, list_fileNames))
dict_list = {}
for el in zipped_list:
    dict_list[str(el[0])] = f'{el[2]}\n {el[0]}\n {el[1]}\n'

with open('Task3 files/result(1.txt+2.txt+3.txt).txt', 'w', encoding='utf8') as f:
    for i in dict_list:
       f.write(dict_list[i])

