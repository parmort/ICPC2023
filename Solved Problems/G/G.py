line = input().split()
row = int(line[0])
col = int(line[1])
total = row * ((row-1) ** (col-1))
print(total%998244353)