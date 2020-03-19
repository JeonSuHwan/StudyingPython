#Defining a basic pie chart (with just one line)
import matplotlib.pyplot as plt

values1=[1,5,8,9,2,0,3,10,4,7]
exp=[0,0,0.2,0.5,0,0,0,0.5,0,0] # 파이조각을 얼만큼 빼낼것인지 지정
# Set the range of value
plt.pie(values1,explode=exp,autopct="%.1f%%")
plt.title("MatPlotLib first plot") # Naming title

plt.show()
