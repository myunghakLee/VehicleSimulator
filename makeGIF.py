import imageio
import numpy as np 
import matplotlib.pyplot as plt


class makeGIF:
    def __init__(self, axis,title,fontsize = 15, figsize = (5,5)):
        self.figure = []
        self.axis = axis
        self.figsize = figsize
        self.title = title
        self.fontsize = fontsize
        pass

    def figure_to_array(self,fig):
        fig.canvas.draw()
        return np.array(fig.canvas.renderer._renderer)
    
    def add_plot(self,Ax,Ay,Bx,By, Azorder=1, Bzorder = 1, Acolor='blue',Bcolor = 'red'):
        f = plt.figure(figsize = self.figsize)
        plt.title(self.title,fontsize= self.fontsize)
        plt.axis(self.axis)
        plt.plot(Ax,Ay,color=Acolor, label="A", zorder = Azorder)
        plt.plot(Bx,By,color=Bcolor, label="B", zorder = Bzorder)
        plt.scatter(Ax[-1], Ay[-1],color=Acolor, zorder = 10)
        plt.scatter(Bx[-1], By[-1],color=Bcolor, zorder = 10)
        plt.legend(loc='upper right')
        plt.close()
        self.figure.append(self.figure_to_array(f))
    
    def make_gif(self,file_name, fps = 10):
        imageio.mimsave(f'{file_name}.gif', self.figure, fps=fps)#     print("=" * 100)

# +
# x = [i for i in range(50)]
# y = [i*2 for i in x]
# GIF = MakeGIF(axis = [0,100,0,100])
# for i in range(1,50):
#     GIF.add_plot(x[:i], y[:i],'blue')
# GIF.make_gif("test")
# -




