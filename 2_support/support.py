from mrjob.job import MRJob
from mrjob.step import MRStep

import sys

# change item _set list into your desire item. eg. ['Bread']
item_set = ['Pastry', 'Bread']

class support(MRJob):
    SORT_VALUES = True

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_count,
                   reducer=self.reducer_count_support),
            MRStep(reducer=self.reducer_compute_support)
        ]

    def mapper_get_count(self, _, line):
        items = eval(line)

        yield ['total'], 1
        if set(item_set).issubset(items):
            yield item_set, 1
        else:
            yield item_set, 0

    def reducer_count_support(self, key, values):
        yield 'support', (key, sum(values))

    def reducer_compute_support(self, keys, values):
        item_value = None
        for key, value in values:
            if key != ['total']:
                item_value = value
                item_name = key
            else:
                percent = str( format(( item_value/value * 100 ),'.2f') ) + "%"
                support_key = "support(" + ", ".join(item_set) + ")"
                yield support_key, percent


if __name__ == '__main__':
    support.run()