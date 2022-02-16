from collections import defaultdict
class ExtractGraph:

    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "data//assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        self.graph = defaultdict(lambda: defaultdict(int))
        self.vaca = defaultdict(lambda: defaultdict(int))
        self.data = []
        self.txt = self.extract_str() # return a list which contains all of documents --- each element is a doucment
        self.est_graph(self.txt)

        return

    def extract_str(self, sentences_add = sentences_add):
        with open(sentences_add,'r') as f :
            txt = f.read()
        txt = txt.split('\n')
        return txt

    def est_graph(self,txt):
        for i in txt:     # get the whole pre-next relationship among corpus
            cur_txt = i.split(' ')
            n = len(cur_txt)
            for j in range(n-1):

                self.vaca[cur_txt[j]][cur_txt[j+1]] += 1
        for i in self.vaca:
            cur_pre = i
            cur_tot_next = sum(self.vaca[cur_pre].values())

            for j in self.vaca[cur_pre]:
                # if i =="<s>":
                #     print(i,j)
                self.graph[cur_pre][j]= self.vaca[cur_pre][j]/cur_tot_next

        return




    def est_graph_1(self, txt):    # a wrong version --- which calculate a wrong probability (use the number of total words)
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
