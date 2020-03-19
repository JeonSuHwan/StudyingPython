#Defining a basic scatter (with just one line)
import matplotlib.pyplot as plt

values1=[1,5,8,9,2,0,3,10,4,7]
values2=[3,8,9,2,1,2,4,7,6,6]
# Set the range of value, color, width of line, linestyle, and vertex shape
plt.scatter(range(1,11),values1,color='g',linewidth=2,linestyle='--',marker='d'
         ,label='value_a') # name of line
plt.scatter(range(1,11),values2,color='r',linewidth=2,linestyle='dashdot',marker='s'
         ,label="values_b")
plt.title("MatPlotLib first plot") # Naming title
plt.grid(True) # create grid
plt.xlabel("month") # the name of x-axis
plt.ylabel("value") # the name of y-axis
plt.legend() # 범례를 화면에 띄움

plt.show()
