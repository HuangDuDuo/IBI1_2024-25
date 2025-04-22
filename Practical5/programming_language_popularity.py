#get dictionary and print
Lan = {'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5}
print (Lan)
import matplotlib
import matplotlib.pyplot as plt
#set x-axis and y-axis
language = list(Lan.keys())
values = list(Lan.values())
#draw bar plot
plt.bar(language,values)
plt.title('Programming language popularity')
plt.xlabel('Language')
plt.ylabel('Users (percentage)')
plt.show()
#print percentage
a = input("Input language:")
print ("The percentage of developers who use", a, "is", Lan[a], ".")
