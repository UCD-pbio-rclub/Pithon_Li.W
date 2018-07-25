import string
import urllib.request

def webFastaCount():
    filename = input('Enter URL: ')
    try:
        with urllib.request.urlopen(filename) as f:
            count = 0
            line = f.readline().decode()
            while line != '':
                if line.startswith('>'):
                    count += 1
                line = f.readline().decode()
            print('There are', count, 'fasta records in this file')
    except:
        print('URL could not be reached')
