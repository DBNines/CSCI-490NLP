import collections
import random

def getTextFromFile(filePath): #open and read file
    with open(filePath, 'r') as file:
        return file.read()

def tokenize(inputText):
    text = inputText.lower() #make all lowercase
    punctuation = '.,!?;:"()[]{}'
    for char in punctuation: #remove punctutation
        text = text.replace(char, "")
        tokens = text.split() #split up tokens by space
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
    sorted_probs = sorted(inputProb.items(), key=lambda x: x[1], reverse=True) #sort list
    print("Top 5 Bigrams are:")
    for i in range(0,5):
        print(sorted_probs[i])

def perplexity(inputTestTokens, inputBiGram):
    biGrams = []
    for i in range(len(inputTestTokens) - 1):
        biGrams.append((inputTestTokens[i], inputTestTokens[i+1])) #Turn test tokens into bigram (maybe make this a function?)

    P = 1.0   # P(w1...wN) for function
    N = len(biGrams) #number of biGrams in test sentence

    for bg in biGrams:
        if bg in inputBiGram:
            prob = inputBiGram[bg]
        else:
            prob = 0.0000000001  # avoid zero
        P = P * prob   # multiply probabilities

    perplex = (1 / P) ** (1 / N) #Same as root-N of 1/P
    return perplex

def buildNGramModel(tokens, n): #n: 2 foor bigram, 3 for trigram mode
    model = collections.defaultdict(list)

    for i in range(len(tokens) - n + 1):
        key = tuple(tokens[i:i+n-1])      
        next_word = tokens[i+n-1]        
        model[key].append(next_word)

    return model

def generateSentence(model, n, length=10):
    start = random.choice(list(model.keys()))
    sentence = list(start)

    for i in range(length - (n-1)):
        key = tuple(sentence[-(n-1):])
        if key in model:
            next_word = random.choice(model[key])
            sentence.append(next_word)
        else:
            break

    return " ".join(sentence)

def main():
    tokens = tokenize(getTextFromFile('input.txt'))
    biGramProbs = biGramProb(tokens)
    getTop5(biGramProbs)
    #Laplace
    biGramProbsLaplace = biGramProbLaplace(tokens)
    print("################" + '\n' + "LAPLACE PROBS")
    getTop5(biGramProbsLaplace)
    print("################" + '\n' + "PERPLEXITY")
    testTokens = tokenize("you should inform your head ta if you are ill") #test sentence/corpus
    perplexityProb = perplexity(testTokens, biGramProbsLaplace)
    print("Perplexity:", perplexityProb)
    print("################" + '\n' + "TEXT GENERATION (BIGRAM)")
    n = 2 #SET THIS to 2 FOR BIGRAM. SET TO 3 FOR TRIGRAM#
    model = buildNGramModel(tokens, n)
    for i in range(0,3): #Increase last number for more sentences
        print(str(i) + ": " + generateSentence(model, n))
    
    print("################" + '\n' + "TEXT GENERATION (TRIGRAM)")
    n = 3 #SET THIS to 2 FOR BIGRAM. SET TO 3 FOR TRIGRAM#
    model = buildNGramModel(tokens, n)
    for i in range(0,3): #Increase last number for more sentences
        print(str(i) + ": " + generateSentence(model, n))

main()