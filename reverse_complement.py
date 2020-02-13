def reverse_complement(st):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rc_string = ''
    for x in st:
        rc_string = complement[x] + rc_string    # adding to beginning of string to reverse
    return rc_string


print(reverse_complement('ACCGTCG'))
