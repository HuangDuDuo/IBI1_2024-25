# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
beta,gamma = 0.3,0.05
for Ra in range(0,101,10):
    N,I,R = 10000,1,0
    V = int(N*Ra/100)
    S = N-V-I
    if S < 0:
        S = 0
    Infected = []
    Susceptible = []
    Recovered = []
    for i in range (1001):
        Infected.append(I)
        Susceptible.append(S)
        Recovered.append(R)
        prob = beta*I/N
        n1 = np.random.choice(range(2),size=S,p=[1-prob,prob])
        In = np.sum(n1)
        n2 = np.random.choice(range(2),size=I,p=[1-gamma,gamma])
        Re = np.sum(n2)
        R = R+Re
        I = I+In-Re
        S = S-In
    plt.plot(Infected,label=f"{Ra}%")
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()