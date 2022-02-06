import StringDouble
import ExtractGraph

import heapq
import numpy as np


class Beam(object):
    # For comparison of prefixes, the tuple (prefix_probability, complete_sentence) is used.
    # This is so that if two prefixes have equal probabilities then a complete sentence is preferred over an incomplete one since (0.5, False) < (0.5, True)
    def __init__(self, beam_width):
        self.heap = list()
        self.beam_width = beam_width

    def add(self, prob, complete, prefix):
        heapq.heappush(self.heap, (prob, complete, prefix))
        if len(self.heap) > self.beam_width:
            heapq.heappop(self.heap)

    def __iter__(self):
        return iter(self.heap)

class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        sentence = ""
        probability = 0.0
        res = self.beamSearchV2( pre_words, beamK, 0, maxToken)
        return res

        #return StringDouble.StringDouble(sentence, probability)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        sentence = ""
        probability = 0.0
        prev_beam = Beam(beamK)
        prev_beam.add(probability, False, pre_words)

        while True:
            curr_beam = Beam(beamK)
            count = 0
            # Add complete sentences that do not yet have the best probability to the current beam, the rest prepare to add more words to them.
            for (prefix_prob, complete, prefix) in prev_beam:
                num = len(prefix.split(' '))
                if complete == True:
                    count +=1
                    curr_beam.add(prefix_prob, True, prefix)
                    continue
                    #
                elif len(prefix.split(' '))==maxToken:
                    count+=1
                    curr_beam.add(prefix_prob, False, prefix)
                    continue

                else:
                    for (next_word,next_prob) in self.graph.graph[prefix.split(' ')[-1]].items():
                        if next_word == '</s>':  # if next word is the end token then mark prefix as complete and leave out the end token
                            denominator = (num + 1) ** param_lambda
                            a = np.log(next_prob)
                            prob = (num**param_lambda)
                            prob = prob * prefix_prob
                            curr_beam.add((prob + a)/denominator, True, prefix+' '+next_word)
                        else:  # if next word is a non-end token then mark prefix as incomplete
                            denominator = (num+1)**param_lambda
                            a = np.log(next_prob)
                            prob = (num ** param_lambda)
                            prob = prob * prefix_prob
                            curr_beam.add((prob+ a)/denominator, False, prefix +' '+next_word)

            (best_prob, best_complete, best_prefix) = max(curr_beam)


            # if best_complete==True or len(best_prefix.split(' '))  == maxToken:  # if most probable prefix is a complete sentence or has a length that exceeds the clip length (ignoring the start token) then return it
            #     return StringDouble.StringDouble((best_prefix), best_prob)  # return best sentence without the start token and together with its probability

            if  count == beamK:
                return StringDouble.StringDouble((best_prefix),best_prob)  # return best sentence without the start token and together with its probability


            prev_beam = curr_beam




