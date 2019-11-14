def FCFS(sequence,start):
    temp = sequence.copy()
    temp.insert(0,start)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    size = len(temp)
    x = temp
    y = []
    headmovement = 0
    for i in range(0,size):
        y.append(-i)
        if i!=size-1:
            headmovement = headmovement + abs(temp[i]-temp[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(temp)
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="FCFS")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("First Come First Served Scheduling Algorithm")
    plt.text(172.5, -8.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(172.5, -9.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()