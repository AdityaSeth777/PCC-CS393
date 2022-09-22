def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)

n = int(input("Enter the number of lines to be read -> "))
a=input("Enter the name of the file you want to open: ")
file_read_from_head(a,n)