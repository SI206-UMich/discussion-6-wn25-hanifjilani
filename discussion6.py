import unittest
import os
import csv

def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open
    out_d = {}
    with open(full_path, 'r') as file:
        csvread = csv.reader(file)
        headers = next(csvread)
        out_d['2020'] = {}
        out_d['2021'] = {}
        out_d['2022'] = {}
        for i in csvread:
            out_d['2020'][i[0]] = i[1]
            out_d['2021'][i[0]] = i[2]
            out_d['2022'][i[0]] = i[3]
    return out_d
def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    ans = []
    for year in d:
        maxval = int(d[year]['JAN'])
        month_val = 'JAN'
        for month in d[year]:
            if maxval < int(d[year][month]):
                maxval = int(d[year][month])
                month_val = month
        ans.append((year, month_val, maxval))
    return ans
def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    out_d = {}
    for year in d:
        total = 0.0
        count = 0
        for month in d[year]:
            total += float(d[year][month])
            count += 1
        total = total/count
        total = round(total)
        out_d[year] = total
    return out_d

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)
        print(self.max_tup_list)
    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
