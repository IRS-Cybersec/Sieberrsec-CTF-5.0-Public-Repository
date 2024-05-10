with open('ouroboros.bin', 'rb') as infile:
    binary_data = infile.read()

reversed_data = binary_data[::-1]

with open('ouroboros.pyc', 'wb') as outfile:
    outfile.write(reversed_data)
