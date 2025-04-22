# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N,I,S,R = 10000,1,9999,0
beta,gamma = 0.3,0.05
Infected = []
Susceptible = []
Recovered = []
for i in range (1001):
    Infected.append(I)
    Susceptible.append(S)
    Recovered.append(R)
    prob = beta*I/N
    n1 = np.random.choice(range(2),S,p=[1-prob,prob])
    In = np.sum(n1)
    n2 = np.random.choice(range(2),I,p=[1-gamma,gamma])
    Re = np.sum(n2)
    R = R+Re
    I = I+In-Re
    S = S-In
plt.figure(figsize=(10, 6))
plt.plot(Susceptible,label='Susceptible')
plt.plot(Infected,label='Infected')
plt.plot(Recovered,label='Recovered')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()