def getTextFromFile(filePath):
    with open(filePath, 'r') as file:
        return file.read()

def tokenize(inputText):
    text = inputText.lower()
    punctuation = '.,!?;:"()[]{}'
    for char in punctuation:
        text = text.replace(char, "")
        tokens = text.split()
    return tokens

#def biGramProb(tokens)

def main():
    tokens = tokenize(getTextFromFile('input.txt'))

main()