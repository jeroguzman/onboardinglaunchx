def average(values):
    return sum(values) / len(values)

average([50, 75, 100])

def fuel_read(read1, read2, read3):
    return f'''
    Average fuel: {average([read1, read2, read3])}%
    Read1: {read1}%
    Read2: {read2}%
    Read3: {read3}%
    '''
print(fuel_read(50, 75, 100))

