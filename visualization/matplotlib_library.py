import matplotlib.pyplot as plt

# fig = plt.figure("Histogram")
# ax = fig.add_subplot(1,1,1)
# ax.hist([21,12,23,35,45,60,33,22,56,33,22,99,48,38], bins = 7, facecolor = 'r', normed = True)

# plt.title("Distribution")
# plt.xlabel("Range")
# plt.ylabel("Amount")
# plt.show()

# fig2 = plt.figure('Box-plot')
# ax1 = fig2.add_subplot(1,1,1)
# ax1.boxplot([21, 12, 18, 23, 34, 43, 92, 21, 24, 11])
# plt.show()

# fig3 = plt.figure('Bar')
# ax2 = fig3.add_subplot(1,1,1)
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_title("Bars")
# ax2.bar([1,2,3,4], [5, 10, 15, 5], [0.5, 1, 1, 3],color=['r', 'b'])
# plt.show()

# fig4 = plt.figure('Line')
# ax3 = fig4.add_subplot(1,1,1)
# ax3.set_xlim([-2, 10])
# ax3.set_ylim([0,6])
# ax3.set_xlabel('X')
# ax3.set_ylabel('Y')
# ax3.set_title('Lines')
# ax3.plot([-1, 2, 4, 7, 8], [5, 2, 3, 4, 3], 'r')
# plt.show()


# data = {'Player': ['Lerons', 'James', 'Kobe', 'Curry'],
#         'First':  [10,10,8,2],
#         'Second': [12,8,13,8],
#         'Third': [15,12,8,8],
#         'Fourth': [18,22,4,3]}

# fig5 = plt.figure('Stackted bar')
# ax4 =  fig5.add_subplot(1,1,1)
# bar_width = 0.5
# bars = [i + 1 for i in range(len(data['First']))]
# ticks = [i + (bar_width/ 2) for i in bars]
# ax4.bar(bars, 
#         data['First'], 
#         width = bar_width,
#         label = 'First Quarter', 
#         color = '#AA5439')
# ax4.bar(bars, 
#         data['Second'], 
#         width = bar_width,
#         bottom = data['First'],
#         label = 'Second Quarter',
#         color = '#FFD600')
# ax4.bar(bars, 
#         data['Third'], 
#         width = bar_width,
#         bottom = [i + j for i, j in zip(data['First'], data['Second'])],
#         label = 'Third Quaters',
#         color = '#FF9200')
# ax4.bar(bars,
#         data['Fourth'],
#         width = bar_width,
#         bottom = [i + j + k for i, j, k in zip(data['First'],data['Second'],data['Third'])],
#         label = 'Fourth Quaters',
#         color = 'r')
# plt.xticks(ticks, data['Player'])
# ax4.set_xlabel("Total")
# ax4.set_ylabel("Player")
# plt.legend(loc = 'upper right')
# plt.xlim([min(ticks) - bar_width, max(ticks) + bar_width])
# plt.show()


# fig6 = plt.figure('Scatter')
# ax5 = fig6.add_subplot(1,1,1)
# ax5.scatter([-1,0,2,3,5],[2,1,3,0.5,4],[120,200,300,150,30],['r','g','#BCDFF0','#BB5500'])
# plt.show()

# fig7 = plt.figure('Pie')
# sizes = [50, 50, 44, 36]
# labels = ['Wade', 'James', 'Kobe', 'Curry']
# explode = (0.1, 0, 0, 0)
# colors= ['red', 'purple', 'yellow', 'blue']
# plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
# plt.axis('equal')
# plt.show()