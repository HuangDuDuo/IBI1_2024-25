DNA_seq=input('Please input DNA sequence to be cut: ')
Restriction_seq=input('Please input the sequence recognized by the restriction enzyme: ')
def cut_sites(DNA,Restriction):
    canonical={'A','T','C','G'}
    check=DNA+Restriction
    for a in check:
        if a not in canonical:
            return ('error')
    positions=[]
    for i in range(len(DNA)-len(Restriction)+1):
        if DNA[i:i+len(Restriction)]==Restriction:
            positions.append(i)
    return (positions)
a=cut_sites(DNA_seq,Restriction_seq)
if a==[]:
    print ('No restriction enzyme cut site exists.')
elif a=='error':
    print ('Error nucleotides detected!')
else:
    print (f'Restriction enzyme cut sites are at these places: {a}.')
