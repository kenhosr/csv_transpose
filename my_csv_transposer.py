import csv
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

"""transpose a csv file, usage: python my_csv_transposer.py infile, outfile"""

with open(infile) as f:
    reader = csv.reader(f)
    cols = []
    for row in reader:
        cols.append(row)

with open(outfile, 'wb') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for i in range(len(max(cols, key=len))):
        writer.writerow([(c[i]) for c in cols])
