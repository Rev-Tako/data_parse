import sys
import os
import glob
import re
from os.path import exists


def readfile(directoryname, regfile):
    # filepath = f'{directoryname}/[0-9][0-9][0-9][0-9][0-9][0-9]{regfile}*'
    filepath = f'{directoryname}/[0-9][0-9][0-9][0-9][0-9]{regfile}*'
    print(f'filepattern expected:  {filepath}')
    txt = glob.glob(filepath)
    txt.sort()

    if txt:
        print('successfully started reading directory')
        print(f'files identified: {txt}')
    else:
        print(f'files identified: {txt}')
        print('cannot read files, try again')

    for filename in txt:
        print(f'attempting to read file: {filename}')
        outfile = filename.replace(f'{regfile}*.txt', '').replace(f'{directoryname}/', '').replace(f'.txt', '')[0:6]
        outline = filename.replace(f'{directoryname}/', '')
        with open(filename, 'r') as f:
            print(f'creating output file at: output_csvs/outfile_2.csv')
            if not os.path.isdir('output_csvs'):
                os.mkdir('output_csvs')
            with open(f'output_csvs/outfile_2.csv', 'a+') as fileout:
                print(f'reading: {outline}, saving to outfile_2.csv')
                fileout.seek(0)
                if outline in fileout.read():
                    break
                fileout.write(f'\n{outline},')
                for line in f:
                    if "FEEDBACK:" in line:
                        templine = f'"{line}'
                        newline = re.sub("FEEDBACK: (TP|FP|FN)", '",FEEDBACK: \\1,"', templine)
                        # print(f'line:  {newline}')
                        # print(f'last three:  {newline[-3:]}')
                        # print(f'last two:  {newline[-2]}')
                        # print(f'last one:  {newline[-1]}')
                        # print(newline[-3:] == '["\n')
                        if newline[-3:] == '" \n':
                            newline = newline.rstrip(newline[-1])
                            newline = newline.rstrip(newline[-1])
                            newline = newline.rstrip(newline[-1])
                            newline = newline + ','
                        if newline[-2:] == '"\n':
                            newline = newline.rstrip(newline[-1])
                            newline = newline.rstrip(newline[-1])
                            newline = newline + ','
                    else:
                        newline = line.replace('\n', '')
                        newline = f'"{newline}",'
                    fileout.write(f'{newline}')
    print('process complete')
    return


# def converttocsv():
#     filepath = 'output_txts/*.txt'
#     txt = glob.glob(filepath)
#     txt.sort()
#     # print(txt)
#     for file in txt:
#         newname = file.replace('output_txts/', '')[0:6]
#         # print(newname)
#         with open(file, 'r') as f:
#             linelist = f.readlines()
#             # print(linelist)
#             with open(f'output_csvs/{newname}.csv', 'a+') as newfile:
#                 # print(newfile)
#                 newfile.seek(0)
#                 for line in linelist:
#                     if (line == '\n') or (line == '') or (line == '   \n'):
#                         continue
#                     elif '.txt' in line:
#                         continue
#                     elif line not in newfile:
#                         print('line: ', line)
#                         newfile.write(f"[{line}],")
#     return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(f"attempting to read {sys.argv[1]}")
        try:
            print(f"opening {sys.argv[1]}")
            readfile(directoryname=sys.argv[1], regfile='_Conversation_')
        except Exception as e:
            # handle any other exception
            print('process not complete')
            print(str(e))
    else:
        print("attempting to read test_txts")
        # readfile(directoryname='test_txts', regfile='_Conversation_')
        try:
            print("opening test_txts")
            readfile(directoryname='test_txts', regfile='_Conversation_')   # '~/DEVWEB/2022/nodejs/scratch' ~/DEVWEB/2022/nodejs/scratch  /home/pqb20197/DEVWEB/2022/nodejs/scratch
        except Exception as e:
            # handle any other exception
            print('process not complete')
            print(print(str(e)))

