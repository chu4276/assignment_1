from mrjob.job import MRJob
from mrjob.step import MRStep

class MBADataPreprocessing(MRJob):
    
    d = dict()
    def steps(self):
        return [
            MRStep(mapper=self.mapper_map_transaction_item,
                   reducer=self.reducer_reduce_export_transaction)
        ]

    def mapper_map_transaction_item(self, _, line):
        (Date, Time, Transaction, Item) = line.split(',')
        yield Transaction, Item 

    def reducer_reduce_export_transaction(self, key, values):
        transaction = str(list(values)) + "\n"
        fout_support.write(transaction)
        fout_confidence.write(transaction)
        fout_lift.write(transaction)
        # yield key, list(values)

if __name__ == '__main__':
    fout_support = open('support.txt', 'w')
    fout_confidence = open('confidence.txt', 'w')
    fout_lift = open('lift.txt', 'w')
    MBADataPreprocessing.run()
    fout_support.close()
    fout_confidence.close()
    fout_lift.close()
