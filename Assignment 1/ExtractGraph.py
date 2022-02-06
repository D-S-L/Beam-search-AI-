class ExtractGraph:

    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "data//assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        self.graph = {}
        self.data = []
        self.txt = self.extract_str()
        self.graph = self.est_graph(self.txt)
        #print(self.graph)
        return

    def extract_str(self, sentences_add = sentences_add):
        with open(sentences_add,'r') as f :
            txt = f.read()
        txt = txt.split('\n')
        return txt


    def est_graph(self, txt):
        graph = self.graph
        n  = len(txt)
        s = set()
        for i in range(n):
            cur_doc = txt[i].split(' ')
            s = s.union(set(cur_doc))
        num_total = len(s)
        #print('num_total: ',num_total)

        for i in range(n):
            cur_doc = txt[i].split(' ')

            m = len(cur_doc)
            for j in range(m-1):
                pre = cur_doc[j]
                next = cur_doc[j+1]

                cur_next = graph.get(pre,0)
                if cur_next == 0:
                    graph[pre] = {next:1/num_total}
                else:
                    if next in cur_next:
                        cur = cur_next.get(next,0)*num_total
                        cur +=1
                        cur_next[next] = cur / num_total
                    else:
                        cur_next[next] = 1/num_total
        return graph


    def getProb(self, head_word, tail_word):
        prob = self.graph.get(head_word,0)
        if prob == 0:
            return False
        prob = prob.get(tail_word,0)
        return prob




if __name__ == '__main__':
        graph = ExtractGraph()
        print(graph.graph['said'])
        # Test extraction correctness.
        head_word = "said"
        tail_word = "."
        print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is " + str(graph.getProb(head_word, tail_word)))
        head_word = "Water"
        tail_word = "<s>"
        print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is " + str(graph.getProb(head_word, tail_word)))
        head_word = "planned"
        tail_word = "economy"
        print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is " + str(graph.getProb(head_word, tail_word)))
        head_word = "."
        tail_word = "</s>"
        print("The probability of \"" + tail_word + "\" appearing after \"" + head_word + "\" is "
                        +  str(graph.getProb(head_word, tail_word)))

#
#
