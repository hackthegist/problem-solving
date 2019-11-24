words = ['ba', 'bdca', 'b', 'a','bca','bda']
words2 = ['a','zxb','ba','bca','bda','bdca','zxbe','azxbe','azxpbe']
words3 = ['a','a','bb','bb','ab']
words4 = ['bb', 'addd', 'csss']

def longestChain(words):
    string_chains = {k: 1 for k in words}
    words = sorted(words, key=lambda x: len(x))

    for w in words:
        if len(w) > 1:
            chain = 1
            for i in range(len(w)):
                if i == 0:
                    _w = w[1:]
                elif i == len(w)-1:
                    _w = w[:-1]
                else:
                    _w = w[:i] + w[i+1:]
                if _w in string_chains.keys():
                    chain = string_chains[_w] + 1 if string_chains[_w] + 1 > chain else chain
            string_chains[w] = chain
    return max(string_chains.values())

print(longestChain(words4))

        
            
# def longestChain(words):
#     string_chains = {k: 0 for k in words}
#     words = sorted(words, key=lambda x: len(x))

#     for w in words:
#         if len(w) == 1:
#             string_chains[w] = 1
#         else:
#             chain = 0
#             for ch in w:
#                 _w = w.replace(ch, '')
#                 if _w in string_chains.keys():
#                     chain = string_chains[_w] + 1 if string_chains[_w] + 1 > chain else chain
#             string_chains[w] = chain
#     return max(string_chains.values())