#Read fasta into one line
def read_seq(file):
    sequence=''
    for line in file:
        line=line.strip()
        if not line.startswith('>'):
            sequence+=line
    return sequence

human_fasta=open('P04179.fasta','r')
mouse_fasta=open('P09671.fasta','r')
random_fasta=open('Random_Sequence.fasta','r')
human_seq=read_seq(human_fasta)
mouse_seq=read_seq(mouse_fasta)
random_seq=read_seq(random_fasta)

length=len(random_seq)

#Make a blosum dictionary
blosum={}
BLOSUM62=open('BLOSUM62.txt','r')
for line in BLOSUM62:
    if line.startswith('#') or line.strip()=='':
        continue
    if line.startswith(' '):
        title=line.strip().split()
        total_num=len(title)
    else:
        part=line.strip().split()
        y=part[0]
        for x in range(total_num-1):
            blosum[(title[x],y)]=int(part[x+1])

def calculate(seq1,seq2):
    same_count=0
    score=0
    alignment=''
    for j in range(length-1):
        score+=blosum[(seq1[j],seq2[j])]
        if seq1[j]==seq2[j]:
            same_count+=1
            alignment+='|'
        else:
            alignment+=' '
    percentage=same_count/length
    return score,percentage,alignment

#Print results
score,percentage,alignment=calculate(human_seq,mouse_seq)
print (f'Compare human to mouse:\nscore={score}, percentage={percentage}\nAlignment:')
print (f'{human_seq}\n{alignment}\n{mouse_seq}\n')

score,percentage,alignment=calculate(human_seq,random_seq)
print (f'Compare human to random:\nscore={score}, percentage={percentage}\nAlignment:')
print (f'{human_seq}\n{alignment}\n{random_seq}\n')

score,percentage,alignment=calculate(mouse_seq,random_seq)
print (f'Compare mouse to random:\nscore={score}, percentage={percentage}\nAlignment:')
print (f'{mouse_seq}\n{alignment}\n{random_seq}\n')


