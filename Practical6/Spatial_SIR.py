import numpy as np
import matplotlib.pyplot as plt
population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
beta,gamma = 0.3,0.05
near = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
for time in range(100):
    #print some points
    if time in (0,20,50,99):
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.title('SIR model')
        plt.show()
    I = np.argwhere(population==1)
    #locate places infected
    for Infected in I:
        x, y = Infected
        #locate places to infect
        for nx,ny in near:
            Ix,Iy = x+nx,y+ny
            #check ability
            if 0<=Ix<100 and 0<=Iy<100:
                if population[Ix,Iy] == 0:
                    #possible infection
                    n1 = np.random.choice(range(2),1,p=[1-beta,beta])
                    In = np.sum(n1)
                    population[Ix,Iy] = population[Ix,Iy]+In
        #possible recovery
        n2 = np.random.choice(range(2),1,p=[1-gamma,gamma])
        Re = np.sum(n2)
        population[x,y] = population[x,y]+Re


    