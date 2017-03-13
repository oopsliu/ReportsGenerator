#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import os,sys

# Plot data
def plotLines(type):
	if type == 'cpu':
		fields = ['cpu 1st','cpu 2nd','cpu 3rd']
		title = 'CPU Utilization'
	elif type == 'mem':
		fields = ['mem 1st','mem 2nd','mem 3rd']
		title = 'Memory Utilization'
	
	x = [10,20,30,40,50,60]
	plt.title(title, fontsize=20)
	for rank, column in enumerate(fields):  
		plt.plot(x,  
				patrol_data[column.replace("\n", " ")].values,"o-", markeredgewidth=0.0,ms=10, 
				lw=2.5, color=myColors[rank],label = fields[rank])  
		xlabel=['31','32','35','36','113','114']
		plt.xticks(x,xlabel) 
		y_pos = patrol_data[column.replace("\n", " ")].values[-1] - 0.5  
		if column == "cpu 1st":  
			y_pos += 0.5  
		elif column == "cpu 2nd":  
			y_pos -= 0.5  
		elif column == "cpu 3rd":  
			y_pos += 0.75  
		elif column == "mem 1st":  
			y_pos -= 0.25  
		elif column == "mem 2nd":  
			y_pos += 1.25  
		elif column == "mem 3rd":  
			y_pos += 0.25  
		plt.text(61, y_pos, column, fontsize=14, color=myColors[rank])  
		
	plt.legend()
	plt.savefig(type +".png", bbox_inches="tight")

# Set csv path	
current_dir =  os.path.dirname(__file__)
csvdir = os.path.join(current_dir,'static','csv')
csvfile = csvdir + r'\test.csv'
	
# Read the data into a pandas DataFrame.  
patrol_data = pd.read_csv(csvfile) 
myColors = [ (14, 187, 159), (245, 199, 0),  (239, 72, 54)]  

for i in range(len(myColors)):  
	r, g, b = myColors[i]  
	myColors[i] = (r / 255., g / 255., b / 255.)  

plt.figure(figsize=(12, 14))  

# Remove the plot frame lines. 
ax = plt.subplot(111)  
ax.spines["top"].set_visible(False)  
ax.spines["bottom"].set_visible(False)  
ax.spines["right"].set_visible(False)  
ax.spines["left"].set_visible(False)  
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()  
plt.ylim(0, 100)  
plt.xlim(8, 68)  
plt.yticks(range(0, 101, 10), [str(x) + "%" for x in range(0, 101, 10)], fontsize=14)  
plt.xticks(fontsize=14)  
for y in range(10, 101, 10):  
	plt.plot(range(8, 62), [y] * len(range(8, 62)), "--", lw=0.5, color="black", alpha=0.3)  
plt.tick_params(axis="both", which="both", bottom="off", top="off",  
				labelbottom="on", left="off", right="off", labelleft="on")  


if __name__ == '__main__':
    main()