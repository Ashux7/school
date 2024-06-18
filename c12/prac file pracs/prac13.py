import matplotlib.pyplot as plt
x = [1,2,3]
y=[2,4,1]
plt.plot(x, y, color='b', marker='o', markeredgecolor='k')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title('LINE GRAPH')
plt.savefig('p13.jpg')
plt.show()