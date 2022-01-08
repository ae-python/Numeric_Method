import matplotlib.pyplot as plt

lst = [0, 1, 2]
dic = {0:[1,2,3], 1:[0,0,0], 2:[1,1,1]}

for i in range(3):
    plt.plot(lst,dic[lst[i]])

plt.show()