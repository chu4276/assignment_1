from mrjob.job import MRJob
from mrjob.step import MRStep
from dateutil import parser

class sales_comparison(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_map_by_date,
                   reducer=self.reducer_reduce_by_day),
            MRStep(reducer=self.reducer_reduce_by_date),
            MRStep(mapper=self.mapper_map_day_to_weekday_weekend,
                   reducer=self.reducer_reduce_by_weekday_weekend),
        ]

    def mapper_map_by_date(self, _, line):
        (Date, Time, Transaction, Item) = line.split(',')
        yield Date, 1

    def reducer_reduce_by_day(self, key, values):
        yield parser.parse(key).strftime("%A"), (sum(values), 1)

    def reducer_reduce_by_date(self, key, values):
        sale_total = 0
        day_total = 0
        for s_total, d_total in values:
            sale_total += s_total
            day_total += d_total
        yield key, (sale_total, day_total)

    def mapper_map_day_to_weekday_weekend(self, key, values):
        if(key == "Monday"):
            yield 'weekday', values
        elif(key == "Tuesday"):
            yield 'weekday', values
        elif(key == "Wednesday"):
            yield 'weekday', values
        elif(key == "Thursday"):
            yield 'weekday', values
        elif(key == "Friday"):
            yield 'weekday', values
        else:
            yield 'weekend', values

    def reducer_reduce_by_weekday_weekend(self, key, values):
        sale_total = 0
        day_total = 0
        for s_total, d_total in values:
            sale_total += s_total
            day_total += d_total
        sale_average = sale_total / day_total
        yield key, sale_average

if __name__ == '__main__':
    sales_comparison.run()
