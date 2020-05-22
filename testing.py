import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class RandWalkSim():

    def __init__(self):

        #Creating figures up plot
        self.fig = plt.figure()
        self.p1 = self.fig.add_subplot(111)
        self.p1.set_ylim(-2, 10)
        self.p1.set_xlim(-5, 10)
        plt.title('2D Random Walk')
        #start = path[:1]
        #stop = path[-1:]
        #p1.plot(start[:,0], start[:,1],c='red', marker='o')
        #p1.plot(stop[:,0], stop[:,1],c='black', marker='o')
        self.xdata, self.ydata = [], []

    def rand_walk(self):
        #setting up steps for simulating 2D 
        self.dims = 2
        step_n = 5
        step_set = [-1, 0, 1]
        origin = np.zeros((1,self.dims))

        # Simulate steps in 2D
        step_shape = (step_n,self.dims)
        steps = np.random.choice(a=step_set, size=step_shape)
        path = np.concatenate([origin, steps]).cumsum(0)
        return path
        
    #This function returns a tuple containing elements of random walk path 
    def data_extract(self, path):
        for pos in range(len(path)):
            sample = path[pos]
            print("data extract:", sample[0], "&", sample[1])
            yield sample[0], sample[1]

    def resize_plot(self, xmin, xmax,ymin, ymax, t, y):
        #Below code of if statements are to re-size the simulation if the random walk goes out of the frame
        if t >= xmax:
            self.p1.set_xlim(1.1*xmin, 1.1*xmax)
            self.p1.figure.canvas.draw()

        if t < xmin:
            self.p1.set_xlim(1.1*xmin, 1.1*xmax)
            self.p1.figure.canvas.draw()

        if y <= ymin:
            self.p1.set_ylim(1.1*ymin, 1.1*ymax)
            self.p1.figure.canvas.draw()
        
        if t >= ymax:
            self.p1.set_ylim(1.1*ymin, 1.1*ymax)
            self.p1.figure.canvas.draw()     

    def animate(self, data):
        #get data from path using function and 
        t, y = data
        
        self.xdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.xdata,self.ydata)
        xmin, xmax = self.p1.get_xlim()
        ymin, ymax = self.p1.get_ylim()
        
        self.resize_plot(xmin, xmax, ymin, ymax, t, y)
        self.line.set_data(self.xdata, self.ydata)

        return self.line,

    def anim_sim(self, color="blue"):
        print("starting...")

        #Step 1: use rand_walk to generate unique random walk path. This path will into data_extract method for extraction
        rand_path = self.rand_walk()
        print("path data:", rand_path)

        #Step 2: Create a plot and lines for each random paths
        self.plt_col = color

        self.line, = self.p1.plot([],[], c=self.plt_col)
        print(self.line,)

        #Step 3: clear existing data 
        del self.xdata[:]
        del self.ydata[:]
        self.line.set_data(self.xdata, self.ydata)

        #step 4: run animations
        self.anim = animation.FuncAnimation(self.fig, self.animate, self.data_extract(rand_path),
                                         blit=True, interval=10, repeat=False)#savecount=210)
        print("exiting anim")
        return self.anim

    #animation.FFMpegWriter()
    #anim.save('randomwalk.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    #anim.save('randomwalk.mp4',fps=30, writer='ffmpeg')
    #anim.save('randomwalk10000.gif', writer='imagemagick')


#Instantiating above class
simulate = RandWalkSim()

anim1 = simulate.anim_sim(color="red")
anim2 = simulate.anim_sim(color="yellow")
anim3 = simulate.anim_sim(color="orange")

plt.show()


