from mrjob.job import MRJob
from mrjob.step import MRStep

import sys

# change antecedent and consequent lists to find confidence of your desire itemset
antecedent = ['Chicken sand']
consequent = ['Coffee']


support_ant_con = antecedent + consequent
support_ant = antecedent

class confidence(MRJob):
    SORT_VALUES = True

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_count,
                   reducer=self.reducer_count_support),
            MRStep(reducer=self.reducer_compute_confidence)
        ]

    def mapper_get_count(self, _, line):
        items = eval(line)
        
        # change item list into your desire item. eg. ['Bread']

        yield ['total'], 1

        if set(support_ant_con).issubset(items):
            yield support_ant_con, 1
        else:
            yield support_ant_con, 0

        if set(support_ant).issubset(items):
            yield support_ant, 1
        else:
            yield support_ant, 0


    def reducer_count_support(self, key, values):
        yield 'confidence', (key, sum(values))

    def reducer_compute_confidence(self, keys, values):
        item_value = None
        for key, value in values:
            if key == support_ant_con:
                antecedent_count = value
            elif key == support_ant:
                consequent_count = value
            else:
                total_count = value
                
        support_antecedent = antecedent_count / total_count
        support_consequent = consequent_count / total_count
        percent = str( format(( support_antecedent / support_consequent * 100 ),'.2f') ) + "%"
        confidence_key = "confidence(" + ", ".join(antecedent) + " --> " + ", ".join(consequent) + ")"
        yield confidence_key, percent


if __name__ == '__main__':
    confidence.run()