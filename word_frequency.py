import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
] 


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

    
f=open(file,"r" )
data=f.read()
wordlist=data.split()
newlist={}

for words in wordlist:
    wordsl=words.lower()
    wordsla=wordsl.translate(str.maketrans('','',string.punctuation))
    occurences= data.count(wordsla)
    starnote=(int(occurences)* "*")
    if wordsla in STOP_WORDS:
        continue
    
    if wordsla not in newlist:
        newlist[wordsla] = 1
        continue
    newlist[wordsla]+=1

sorted_newlist =dict(sorted(newlist.items(), key=lambda item: item[1], reverse=True))

keys = sorted_newlist.keys()
for key in keys:
    print(f"{key:<15}" +"|" + f"{sorted_newlist[key]:<5}" + "*" * sorted_newlist[key])

       
       
                
      

