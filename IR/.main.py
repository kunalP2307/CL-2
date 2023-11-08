from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

documents = [
    'The quick brown fox jumped over the lazy dog.',
    'The lazy dog slept in the sun.'
]

tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))
unique_terms = []

for i in range(0, len(documents)):
    documents[i] = tokenizer.tokenize(documents[i])
    temp = []
    for word in documents[i]:
        if word.lower() not in stop_words:
            temp.append(word.lower())
            if word not in unique_terms:
                unique_terms.append(word.lower())
    documents[i] = temp

print(documents)

inverted_list = {}
for term in unique_terms:
    doc_list = []
    for i in range(0, len(documents)):
        if term in documents[i]:
            doc_list.append('Document '+ str(i+1))
    inverted_list[term] = doc_list


def retrieve_docs(term):
    if term in inverted_list:
        return inverted_list[term]
    else:
        return -1


print("Terms    ->      Documents")
for key,values in inverted_list.items():
    print(key + '\t -> ' + ' ,'.join(values))

term = input("Enter keyword to retrieve documents ")
output = retrieve_docs(term)

if output == -1:
    print("No Document is present")
else:
    print(" , ".join(output))
