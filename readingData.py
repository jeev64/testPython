import csv

with open(r'C:\Users\jeeva\OneDrive\Desktop\python1\certificates.csv') as fp:
    reader = csv.reader(fp, delimiter='$')
    next(reader)
    for index, values in enumerate(reader):
        name, certs_num, months_num = values
        print(f"{name} earned {certs_num} certificates in {months_num} months")
