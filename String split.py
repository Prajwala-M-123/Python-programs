def chars_mix_up(a,b):
    #Below function swaps the first two characters ofthe string
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b #final concatenated result
#print the result
print(chars_mix_up('abc','xyz'))
