import matplotlib.pyplot as plt
import csv

from numpy import double

def hetero():
    font = {
        'weight': 'bold',
        'size': 10}

    plt.rc('font', **font)
    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0
    with open('arate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    for r in range(len(t15)):
        print(r, t15[r])
    print(len(t15))

    with open('crate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            s1 += 5
            lamda1.append(double(row[1]))
    for r in range(len(t1)):
        print(r, t1[r])
        print(len(t1))
    with open('replicas2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t5.append(s5)
            s5 += 5
            lamda5.append(double(row[1]))
    for r in range(len(t5)):
        print(r, t5[r])
        print(len(t5))

    fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx()
    # ax1.plot(t5, lamda5, color='blue', label='arrival rate')
    # ax1.plot(t15, lamda15, color='red', label='consumption rate')
    # ax1.plot(t1, lamda1, color='black', label='Max consumption rate')
    rep = []
    for r in lamda5:
        var = r / 95
        rep.append(var)

    ax1.plot(t15, lamda15, label='arrival rate')
    ax1.plot(t1, lamda1, label='consumption rate')
    ax1.plot(t5, lamda5, label="max consumption rate")


   # ax2.plot(t5, rep, label='replicas')
    #
    ax1.set_xlabel('Time (sec)', font=font)
    ax1.set_ylabel('Event Arrival/consumption Rate', font=font)
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    #ax2.set_ylabel('Consumer replicas')
    #
    plt.title('Heterogenous consumers (100, 250 events/sec)')
    ax1.legend()
    #ax2.legend(loc=4)
    #
    plt.show()


def hetero2():


    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0
    with open('arate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    for r in range(len(t15)):
        print(r, t15[r])
    print(len(t15))

    with open('crate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            s1 += 5
            lamda1.append(double(row[1]))
    for r in range(len(t1)):
        print(r, t1[r])
        print(len(t1))
    with open('replicas.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t5.append(s5)
            s5 += 5
            lamda5.append(double(row[1]))
    for r in range(len(t5)):
        print(r, t5[r])
        print(len(t5))

    # fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()
    # ax1.plot(t5, lamda5, color='blue', label='arrival rate')
    # ax1.plot(t15, lamda15, color='red', label='consumption rate')
    # ax1.plot(t1, lamda1, color='black', label='Max consumption rate')
    rep = []
    for r in lamda5:
        var = r / 95
        rep.append(var)

    #ax1.plot(t5, lamda5)

    fig, axs = plt.subplots(2, 1);

    axs[0].plot(t15, lamda15, label='arrival rate')
    axs[0].plot(t1, lamda1, label='consumption rate')
    #axs[0].set_xlabel(('Time (sec)'))
    axs[0].set_ylabel(('Event Arrival/consumption Rate'))




    axs[1].plot(t5, rep, label='replicas')
    #
    axs[1].set_xlabel(('Time (sec)'))
    #plt.set_ylabel('Event Arrival/consumption Rate')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    axs[1].set_ylabel(('Consumer replicas'))
    #
    #plt.title('Bin pack autoscaler')

    #
    plt.show()


def hetero3():


    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0
    with open('arate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    for r in range(len(t15)):
        print(r, t15[r])
    print(len(t15))

    with open('crate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            s1 += 5
            lamda1.append(double(row[1]))
    for r in range(len(t1)):
        print(r, t1[r])
        print(len(t1))
    r100=[]
    r250 = []
    rt = []
    with open('replicas3.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t5.append(s5)
            s5 += 5
            lamda5.append(double(row[1]))
            r100.append(double(row[2]))
            r250.append(double(row[3]))
            rt.append(double(row[2]) + double(row[3]))

    for r in range(len(t5)):
        print(r, t5[r])
        print(len(t5))

    # fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()
    # ax1.plot(t5, lamda5, color='blue', label='arrival rate')
    # ax1.plot(t15, lamda15, color='red', label='consumption rate')
    # ax1.plot(t1, lamda1, color='black', label='Max consumption rate')
    rep = []
    for r in lamda5:
        var = r / 95
        rep.append(var)

    #ax1.plot(t5, lamda5)

    fig, axs = plt.subplots(2, 1)

    axs[0].plot(t15, lamda15, label='arrival rate')
    axs[0].plot(t1, lamda1, label='consumption rate')
    #axs[0].set_xlabel(('Time (sec)'))
    axs[0].set_ylabel(('Event Arrival/consumption Rate'))




    axs[1].plot(t5, rt, color='red', label='replicas')
    # axs[1].plot(t5, r100,color='blue', label='replicas100')
    # axs[1].plot(t5, r250, color='green', label='replicas2500')


    #
    axs[1].set_xlabel(('Time (sec)'), font=font)
    #plt.set_ylabel('Event Arrival/consumption Rate')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    axs[1].set_ylabel(('Consumer replicas'), font=font)
    #
    #plt.title('Bin pack autoscaler')
    axs[1].legend()
    axs[0].legend()

    #
    plt.show()

def hetero3all():


    font = {
            'weight': 'bold',
            'size': 10}

    plt.rc('font', **font)


    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []

    t1 = []
    lamda1 = []

    s15 = 0
    s5 = 0
    s1 = 0
    with open('arate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t15.append(s15)
            s15 += 5
            lamda15.append(double(row[1]))

    for r in range(len(t15)):
        print(r, t15[r])
    print(len(t15))

    with open('crate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t1.append(s1)
            s1 += 5
            lamda1.append(double(row[1]))
    for r in range(len(t1)):
        print(r, t1[r])
        print(len(t1))
    r100=[]
    r250 = []
    rt = []
    with open('replicas3.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # t.append(math.floor(double(row[0])))
            # t.append(str(row[0]))
            t5.append(s5)
            s5 += 5
            lamda5.append(double(row[1]))
            r100.append(double(row[2]))
            r250.append(double(row[3]))
            rt.append(double(row[2]) + double(row[3]))

    for r in range(len(t5)):
        print(r, t5[r])
        print(len(t5))

    # fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()
    # ax1.plot(t5, lamda5, color='blue', label='arrival rate')
    # ax1.plot(t15, lamda15, color='red', label='consumption rate')
    # ax1.plot(t1, lamda1, color='black', label='Max consumption rate')
    rep = []
    for r in lamda5:
        var = r / 95
        rep.append(var)

    #ax1.plot(t5, lamda5)

    fig, axs = plt.subplots(3, 1)

    axs[0].plot(t15, lamda15, label='arrival rate')
    axs[0].plot(t1, lamda1, label='consumption rate')
    #axs[0].set_xlabel(('Time (sec)'))
    axs[0].set_ylabel('Event Arrival/consumption Rate', font=font)




    axs[1].plot(t5, rt, color='red', label='replicas')
    # axs[1].plot(t5, r100,color='blue', label='replicas100')
    # axs[1].plot(t5, r250, color='green', label='replicas2500')


    #
    axs[2].set_xlabel(('Time (sec)'), font=font)
    #plt.set_ylabel('Event Arrival/consumption Rate')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    axs[1].set_ylabel(('Consumer replicas'), font=font)

    ##########################################################################


    axs[2].plot(t5, r100, color='green', label='replicas 100 events/sec')
    axs[2].plot(t5, r250, color='brown', label='replicas 250 events/sec')

    # axs[1].plot(t5, r100,color='blue', label='replicas100')
    # axs[1].plot(t5, r250, color='green', label='replicas2500')


    #
    axs[1].set_xlabel(('Time (sec)'), font=font)
    #plt.set_ylabel('Event Arrival/consumption Rate')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    axs[1].set_ylabel(('Total Consumer replicas'), font=font)

    axs[2].set_ylabel(('Heterogenous Consumer replicas'), font=font)

    #



    #########################################################################


    #
    #plt.title('Bin pack autoscaler')
    axs[1].legend()
    axs[0].legend()
    axs[2].legend()


    #
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #hetero2()
    hetero()
    hetero3()
    hetero3all()


