import random
import matplotlib.pyplot as plt
import numpy as np


"""
This method replicates the random walk concept at 1-dimension level
The black_dot represents the icon that will take the walk. It will be on the 0 position on the integet line Z.
The black dot has equal propability of taking +1 step or a -1 step.
"""
"""
def randomwalk(n):

    black_dot = 0 

    while(n != 0):

        step = random.randint(0,1)  #setting propability 

        if step == 1:
            black_dot += 1  #indicates dot took +1 step
        else:
            black_dot -= 1  #indicates dot took -1 step
        
        n -= 1

    #Plotting on the graph (as this is 1D, just set Y variable as 0)

    data1 = [black_dot, 10]
    data2 = [0,0]

    print(black_dot)
    
    plt.plot(data1,data2)
    plt.show()

     
no_of_steps = 15
randomwalk(no_of_steps)

"""

# Define parameters for the walk
dims = 1
step_n = 10
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))

# Simulate steps in 1D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

print(steps)

# Plot the path
fig = plt.figure(figsize=(8,4),dpi=200)
ax = fig.add_subplot(111)
ax.scatter(np.arange(step_n+1), path, c='blue',alpha=0.25,s=0.05);
ax.plot(path,c='green',alpha=0.5,lw=0.5,ls= '-');
ax.plot(0, start, c='red', marker='+')
ax.plot(step_n, stop, c='black', marker='o')
plt.title('1D Random Walk')
plt.tight_layout(pad=0)
plt.show()
#plt.savefig(‘plots/random_walk_1d.png’,dpi=250);
