from itertools import count as countIter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class GlobalData:

    # current x in 3x + 1
    x = 4

    # count to keep track of x

    """ this the starting value of x in animation """
    count = 5

    # lists containing x and y axis value of current 3x + 1
    x_axis = []
    y_axis = []

    # x index , iteration count
    index = countIter()

    # current plot variable
    current = None

    # list containg the current plots of 3x+1 , stored as we need to remove them and re plot current 3x+1 with diff style and move on
    currentPlots = []

    # list containing current labels of 3x+1 , storing since we will be removing them
    currentAnnotate = []



# animation matlab class
class Anim():

    # initialzer for class
    def __init__(self, fig, **kw):
        self.reward=0
        self.ani = FuncAnimation(fig, self.animate, repeat = False) 

    # main animate function
    def animate(self,i):

            # adding the current value of x to xaxis list
            GlobalData.y_axis.append(GlobalData.x)
            GlobalData.x_axis.append(next(GlobalData.index))

            # if odd then x = 3x + 1 else x = x/2
            if((GlobalData.x % 2) != 0):
                GlobalData.x = int((GlobalData.x * 3) + 1)
            else:
                GlobalData.x = int(GlobalData.x / 2)


            # plotting the current data and storing it
            GlobalData.current = plt.plot(GlobalData.x_axis, GlobalData.y_axis , "black")

            GlobalData.currentPlots.append(GlobalData.current)
            

            # plotting the labels
            for x,y in zip(GlobalData.x_axis, GlobalData.y_axis):

                label = "{}".format(y)

                a = plt.annotate(label, # this is the text
                            (x,y), # these are the coordinates to position the label
                            textcoords="offset points", # how to position the text
                            xytext=(0,10), # distance from text to points (x,y)
                            ha='center') # horizontal alignment can be left, right or center
                
                # and storing it
                GlobalData.currentAnnotate.append(a)

            # if we have reached the series end that is 4 2 1 loop

            """you may notice here that the [-2] and [-3] does not raise error instead they just make the equation false but if all raises error then error is raised"""
            if((GlobalData.y_axis[-1] == 1) and (GlobalData.y_axis[-2] == 2) and (GlobalData.y_axis[-3] == 4)):
                
                print("simulated - {} , steps = {} , max = {}".format(GlobalData.count - 1  , len(GlobalData.x_axis) , max(GlobalData.y_axis)))

                time.sleep(1)
                
                # remove all the lines from the current ploted 3x+1

                # as the multiple overlapping plots were made with each iteration
                for i in GlobalData.currentPlots:

                    # removing all lines from iteration
                    while(True):
                        try:
                            lines = i.pop()
                            lines.remove()
                        except IndexError:
                            break
                            
                # removing anotations
                for i in GlobalData.currentAnnotate:
                    i.remove()

                # resetting the lists
                GlobalData.currentPlots = []
                GlobalData.currentAnnotate = []


                # replotting the current 3x+1
                plt.plot(GlobalData.x_axis , GlobalData.y_axis , "--" , alpha=0.3)
                
                # resetting the x and y axis
                GlobalData.x_axis = []
                GlobalData.y_axis = []

                # x = count
                GlobalData.x = GlobalData.count

                # count = count + 1
                GlobalData.count = GlobalData.count + 1

                # reset index
                GlobalData.index = countIter()





# init animation
Anim(plt.gcf())
plt.tight_layout()
plt.show()