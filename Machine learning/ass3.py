import matplotlib.pyplot as plt

wtimes = [43.1,35.6,37.6,36.5,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,25.6,45.2,54.1,45.6,36.5,43.1]

numOfCust = list(range(1,21))

interval=[]

for x in range(4,13):
    interval.append(x*5)
print (interval)

plt.hist(wtimes, interval, histtype='bar',rwidth=0.8,label="Times")

plt.xlabel('Time spent in seconds')
plt.ylabel('Amount of customers')

plt.legend()
plt.show()

input("Press a key for a pie\n")

nums = [4,5,6,1,4]
genres = ["Comedy","Action","Romance","Drama","SciFi"]
plt.pie(nums,None,labels=genres)
plt.show()