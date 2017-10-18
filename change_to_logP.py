#!usr/bin/python3
#coding=utf-8
#这个脚本用来整理emmax的结果，整理后输出的文件可以用来查找P值对应的position或者用于做图
#这个脚本产生的*_logP 文件可以用来查找P大于某阈值的SNP，*_logP_for_figure 文件用来配合作图脚本作图
import datetime
import math
end1 = 307041717
end2 = 244442276 + end1
end3 = 235667834 + end2
end4 = 246994605 + end3
end5 = 223902240 + end4
end6 = 174033170 + end5
end7 = 182381542 + end6
end8 = 181122637 + end7
end9 = 159769782 + end8

start = datetime.datetime.now()
fl = input('Please enter the file name you want to format: ')
n = fl + '_logP'
m = fl + '_logP_for_figure'
output1 = open(n, 'w')
output2 = open(m, 'w')
print('reading data')
for i in open(fl):
    ii = i.strip().split('\t')
    a = ii[0].split('_')
    ii[2] = str(math.log10(float(ii[2])) * -1)
    b = a + ii
    output1.write('\t'.join(b)+'\n')
    if b[0] == '1':
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '2':
        b[1] = str(int(b[1]) + end1)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '3':
        b[1] = str(int(b[1]) + end2)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '4':
        b[1] = str(int(b[1]) + end3)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '5':
        b[1] = str(int(b[1]) + end4)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '6':
        b[1] = str(int(b[1]) + end5)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '7':
        b[1] = str(int(b[1]) + end6)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '8':
        b[1] = str(int(b[1]) + end7)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '9':
        b[1] = str(int(b[1]) + end8)
        output2.write('\t'.join(b)+'\n')
    elif b[0] == '10':
        b[1] = str(int(b[1]) + end9)
        output2.write('\t'.join(b)+'\n')
end = datetime.datetime.now()
used = (end - start).seconds
print(used,'seconds was used.')
print('done')
