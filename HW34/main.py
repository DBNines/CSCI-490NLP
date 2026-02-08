import collections

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

def biGramProb(inputTokens):
    biGrams = []
    for i in range(len(inputTokens) - 1):
        biGrams.append((inputTokens[i], inputTokens[i+1]))
    uniGramCount = collections.Counter(inputTokens)
    biGramCount = collections.Counter(biGrams)
    #print(biGramCount)#print(uniGramCount)
    probs = {}
    for biGram, count in biGramCount.items():
        probs[biGram] = count / uniGramCount[biGram[0]]
    #print(probs)
    return probs

def biGramProbLaplace(inputTokens):
    biGrams = []
    for i in range(len(inputTokens) - 1):
        biGrams.append((inputTokens[i], inputTokens[i+1]))
    uniGramCount = collections.Counter(inputTokens)
    biGramCount = collections.Counter(biGrams)
    v = len(uniGramCount) # Number of unique words
    probsLaplace = {}
    for biGram, count in biGramCount.items():
        probsLaplace[biGram] = (count + 1) / (uniGramCount[biGram[0]] + v)
    #print(probs)
    return probsLaplace

def getTop5(inputProb):
    sorted_probs = sorted(inputProb.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 Bigrams are:")
    for i in range(0,5):
        print(sorted_probs[i])


def main():
    tokens = tokenize(getTextFromFile('input.txt'))
    biGramProbs = biGramProb(tokens)
    getTop5(biGramProbs)
    #Laplace
    biGramProbsLaplace = biGramProbLaplace(tokens)
    print("################" + '\n' + "LAPLACE PROBS")
    getTop5(biGramProbsLaplace)
    print("################" + '\n' + "PERPLEXITY")

main()