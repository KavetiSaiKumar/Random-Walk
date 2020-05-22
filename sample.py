import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


def randomwalksimulate():
    #setting up steps for simulating 2D 
    dims = 2
    step_n = 150
    step_set = [-1, 0, 4]
    origin = np.zeros((1,dims))

    # Simulate steps in 2D
    step_shape = (step_n,dims)
    steps = np.random.choice(a=step_set, size=step_shape)
    path = np.concatenate([origin, steps]).cumsum(0)
    return path


def prepareplot():
    #plot the figure
    p1 = fig.add_subplot(111)
    p1.set_ylim(-5, 10)
    p1.set_xlim(-5, 10)
    p1.set_xticks(np.arange(-15, 300, step = 3))
    plt.title('2D Random Walk')

    return p1


#This function returns a tuple containing elements of random walk path 1,2,3 
def data_extract(path):
    for pos in range(len(path)):
        sample = path[pos]
        yield sample[0], sample[1]

#below code of if statements are to re-size the simulation if the random walk goes out of the frame
def resize_plot(xmin, xmax,ymin, ymax, t, y):
    if t >= xmax:
        p1.set_xlim(1.1*xmin, 1.1*xmax)
        p1.figure.canvas.draw()

    if t < xmin:
        p1.set_xlim(1.1*xmin, 1.1*xmax)
        p1.figure.canvas.draw()

    if y <= ymin:
        p1.set_ylim(1.1*ymin, 1.1*ymax)
        p1.figure.canvas.draw()
    
    if t >= ymax:
        p1.set_ylim(1.1*ymin, 1.1*ymax)
        p1.figure.canvas.draw()

def run_animation_1(data):
    #will get list of plots data from updateAll
    t, y = data
    #print("t,y values are:", t ," ", y)
    
    xdata.append(t)
    ydata.append(y)
    line1.set_data(xdata,ydata)
    xmin, xmax = p1.get_xlim()
    ymin, ymax = p1.get_ylim()
    
    resize_plot(xmin, xmax, ymin, ymax, t, y)
    line1.set_data(xdata, ydata)

    return line1,

def run_point_animation_1(data):
    #will get list of plots data from updateAll
    t, y = data
    
    xdata.append(t)
    ydata.append(y)
    point1.set_data(xdata,ydata)
    xmin, xmax = p1.get_xlim()
    ymin, ymax = p1.get_ylim()
    
    resize_plot(xmin, xmax, ymin, ymax, t, y)
    point1.set_data(xdata, ydata)

    return point1,

def run_point_animation_2(data):
    #will get list of plots data from updateAll
    t, y = data
    
    xdata1.append(t)
    ydata1.append(y)
    point1.set_data(xdata,ydata)
    xmin, xmax = p1.get_xlim()
    ymin, ymax = p1.get_ylim()
    
    resize_plot(xmin, xmax, ymin, ymax, t, y)
    point1.set_data(xdata1, ydata1)

    return point1,

def run_point_animation_3(data):
    #will get list of plots data from updateAll
    t, y = data
    
    xdata2.append(t)
    ydata2.append(y)
    point2.set_data(xdata,ydata)
    xmin, xmax = p1.get_xlim()
    ymin, ymax = p1.get_ylim()
    
    resize_plot(xmin, xmax, ymin, ymax, t, y)
    point2.set_data(xdata2, ydata2)

    return point2,

def run_animation_2(data):
    #will get list of plots data from updateAll

    t, y = data
    
    xdata1.append(t)
    ydata1.append(y)
    line2.set_data(xdata1,ydata1)
    xmin, xmax = p1.get_xlim()
    ymin, ymax = p1.get_ylim()
    
    resize_plot(xmin, xmax, ymin, ymax, t, y)
    line2.set_data(xdata1, ydata1)

    return line2,

def run_animation_3(data):
    #will get list of plots data from updateAll
    t, y = data
    
    xdata2.append(t)
    ydata2.append(y)
    line3.set_data(xdata2,ydata2)
    xmin, xmax = p1.get_xlim()
    ymin, ymax = p1.get_ylim()
    
    resize_plot(xmin, xmax, ymin, ymax, t, y)
    line3.set_data(xdata2, ydata2)

    return line3,


def update_all(data1, line1, data2, line2):
    update(num, data1, line1)
    update(num, data2, line2)


#Step 1: use randomwalksimulate to generate three unique random walk paths
path = randomwalksimulate()
path1 = randomwalksimulate()
path2 = randomwalksimulate()

start = path[:1]
stop = path[-1:]

#Step 2: Create a plot and lines for each random paths
p1 = prepareplot()

line1, = p1.plot([],[], c='r')
point1, = p1.plot([],[], 'o', c='r')
line2, = p1.plot([],[], c='g')
point2, = p1.plot([],[], 'o', c='g')
line3, = p1.plot([],[], c='b')
point3, = p1.plot([],[], 'o', c='b')


#Step 3: create 3 lists for each random walk for each random walk
xdata, ydata = [], []
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []

#step 4: run animations

intrvl = 150
anim = animation.FuncAnimation(fig, run_animation_1, data_extract(path), interval=intrvl, repeat=False)
point_anim = animation.FuncAnimation(fig, run_point_animation_1, data_extract(path), interval=intrvl, repeat=False)

anim1 = animation.FuncAnimation(fig, run_animation_2, data_extract(path1), interval=intrvl, repeat=False)
point_anim1 = animation.FuncAnimation(fig, run_point_animation_2, data_extract(path1), interval=intrvl, repeat=False)

anim2 = animation.FuncAnimation(fig, run_animation_3, data_extract(path2), interval=intrvl, repeat=False)
point_anim2 = animation.FuncAnimation(fig, run_point_animation_3, data_extract(path2), interval=intrvl, repeat=False)

anim = animation.FuncAnimation(fig, run_animation_1, fargs=(data_extract(path), data_extract(path1), data_extract(path2) ), interval=intrvl, repeat=False)
anim.save('rand.gif', writer='imagemagick')

#plt.show()

#To save the simulation or plot in various formats
#animation.FFMpegWriter()
#anim.save('rando.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#anim.save('rando.mp4',fps=30, writer='ffmpeg')

