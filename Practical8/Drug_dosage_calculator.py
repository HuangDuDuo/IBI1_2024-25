wei = float(input('Please input weight in kg: (number only)'))
stren = input('Please input strength of paracetamol (A=120mg/5ml or B=250mg/5ml):')
def calculate_dosage(weight,strength):
    dose=15
    if weight<10 or weight>100:
        return ('Error weight')
    if strength=='120mg/5ml' or strength=='A':
        stre=120
    elif strength=='250mg/5ml'or strength=='B':
        stre=250
    else:
        return ('Error strength of paracetamol')
    dosage=weight*dose*5/stre
    b='The drug dosage is '+str(dosage)+' ml.'
    return (b)
a=calculate_dosage(wei,stren)
print (a)
    