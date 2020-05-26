import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
no_of_steps = 50

def randomwalksimulate():
    #setting up steps for simulating 2D 
    dims = 2
    step_n = no_of_steps
    step_set = [-1, 0, 1]
    origin = np.zeros((1,dims))

    # Simulate steps in 2D
    step_shape = (step_n,dims)
    steps = np.random.choice(a=step_set, size=step_shape)
    path = np.concatenate([origin, steps]).cumsum(0)
    return path

def prepareplot():
    #plot the figure
    ax = fig.add_subplot(111)
    ax.set_ylim(-2, 10)
    ax.set_xlim(-5, 10)
    #ax.set_xticks(np.arange(-15, 100, step = 10))
    plt.title('Random Walk')

    
    return ax

#This function returns a tuple containing elements of random walk path 1,2,3 
def data_extract():
    path = randomwalksimulate()

    for pos in range(len(path)):
        sample = path[pos]
        yield np.array([ sample[0], sample[1] ])

#below code of if statements are to re-size the simulation if the random walk goes out of the frame
def resize_plot(xmin, xmax,ymin, ymax, t, y):
    if t >= xmax:
        ax.set_xlim(1.1*xmin, 1.1*xmax)
        ax.figure.canvas.draw()

    if t < xmin:
        ax.set_xlim(1.1*xmin, 1.1*xmax)
        ax.figure.canvas.draw()

    if y <= ymin:
        ax.set_ylim(1.1*ymin, 1.1*ymax)
        ax.figure.canvas.draw()
    
    if t >= ymax:
        ax.set_ylim(1.1*ymin, 1.1*ymax)
        ax.figure.canvas.draw()

def run_animation(num, data, line):
    
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    resize_plot(xmin,xmax, ymin, ymax, t=data[0, num-1], y=data[1, num-1])

    line.set_data(data[:2, :num])

def update_all(num, data1, line1, point1, pntline1, 
                    data2, line2,  point2, pntline2, 
                    data3, line3, point3, pntline3, 
                    data4, line4, point4, pntline4):

    run_animation(num, data1, line1)
    run_animation(num, point1, pnt1)
    run_animation(num, data2, line2)
    run_animation(num, point2, pnt2)
    run_animation(num, data3, line3)
    run_animation(num, point3, pnt3)
    run_animation(num, data4, line4)
    run_animation(num, point4, pnt4)


#Step 1: Create a plot and lines for each random paths
# Setting the axes properties
ax = prepareplot()

#step 2: create 4 unique random walk paths(converted to ndarray)
temp1 = np.array(list(data_extract())).T 
temp2 = np.array(list(data_extract())).T 
temp3 = np.array(list(data_extract())).T
temp4 = np.array(list(data_extract())).T

point1 = temp1
point2 = temp2
point3 = temp3
point4 = temp4

line1, = ax.plot([],[], c='#7B56BF', linewidth=3) #lightpurple = #7B56BF
line2, = ax.plot([],[], c='#360259', linewidth=3)
line3, = ax.plot([],[], c='#3e1785', linewidth=3)
line4, = ax.plot([],[], c='#e33341', linewidth=3) #redshade = #e33341

pnt1, = ax.plot([],[], 'o', c='#7B56BF')
pnt2, = ax.plot([],[], 'o', c='#360259')
pnt3, = ax.plot([],[], 'o', c='#3e1785')
pnt4, = ax.plot([],[], 'o', c='#e33341')

#To add gradient
#plotlim = tuple(4*x for x in plt.xlim()) + tuple(7*x for x in plt.ylim())
#test = np.array( [[0,0],[4,1]]).T
#ax.imshow(test, cmap=plt.cm.Greens, interpolation='bicubic', extent=plotlim)  
#plt.draw()  


N = no_of_steps + 2

anim = animation.FuncAnimation(fig, update_all, N,   fargs =(temp1, line1, point1, pnt1, 
                                                             temp2, line2, point2, pnt2, 
                                                             temp3, line3, point3, pnt3,
                                                             temp4, line4, point4, pnt4), 
                                                            interval=150, repeat=False)

#If you want to view the graph, comment out the anim save line and vice versa. 
#This is because both the functions use and flush the data and allowing both lines will cause issues with the later code. 
anim.save('rand.gif', writer='imagemagick')
#plt.show()

#To save the simulation or plot in various formats
#animation.FFMpegWriter()
#anim.save('rando.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#anim.save('rando.mp4',fps=30, writer='ffmpeg')
