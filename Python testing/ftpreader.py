"""
This script is use to check the China server accessibility from outside
"""
import os

# Store directory path of the input files
INPUT_FILE_DIR = raw_input('Enter the directory path of the input files: ')

# Check OS version
if os.name == 'nt':
    INPUT_FILE_DIR = INPUT_FILE_DIR.replace('\\', '\\\\') + '\\\\'
    OUTPUT_FILE_HANDLER = open(os.getcwd() + '\Result.txt', 'a+')
    print('Please check Result.txt in ' + os.getcwd())

elif os.name == 'posix':
    INPUT_FILE_DIR = INPUT_FILE_DIR + '/'
    OUTPUT_FILE_HANDLER = open(os.getcwd() + '/Result.txt', 'a+')
    print('Please check Result.txt in ' + os.getcwd())

FILES_LIST = os.listdir(INPUT_FILE_DIR)
print FILES_LIST

print FILES_LIST[0]

# for eachFile in FILES_LIST:
#     serverName = str(eachFile.replace('.txt', ''))
#     inputFilesHandler = open(INPUT_FILE_DIR + eachFile, 'r')
#     allServersResults = []

#     for eachLine in inputFilesHandler.readlines():
#         pingResult = eachLine
#         pingResult = pingResult.replace('\n', '').replace('\r', '')
#         ipAddress = str(pingResult).split('     ')[0]
#         lossPercentage = str(str(pingResult).split(' (')[1]).replace(' loss),', '')
#         allServersResults.append(ipAddress + '|' + lossPercentage + ',')
#     allServersResults = ''.join(allServersResults)
#     allServersResults = allServersResults[:-1]

#     OUTPUT_FILE_HANDLER.write(serverName + ',' + allServersResults + '\n')

#     inputFilesHandler.close()

# OUTPUT_FILE_HANDLER.close()

