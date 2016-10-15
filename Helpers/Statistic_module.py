# Module that handles the statistic display in the Overview frame
from GUI.OverviewFrame.OverviewFrame import *
from GUI.BottomFrames.ChooserFrame import treeview_hauptwahl,treeview_neben,treeview_haupt
# Other modules should call this method to notify the module that a change in data has occurred

sums=[]
colors=[]
def notify():
    apply_rule()

# Go through the data and calculate credit points
def apply_rule():
    global sums,colors
    sums=[0,0,0]
    colors=['blue','blue','blue']
    for box in semester_boxes:
        for item in box.added_items:
            if item['Tree'] == treeview_haupt:
                sums[0]=sums[0]+int(item['Credits'])
            elif item['Tree'] == treeview_hauptwahl:
                sums[1] = sums[1] + int(item['Credits'])
            elif item['Tree'] == treeview_neben:
                sums[2] = sums[2] + int(item['Credits'])
    # Check of rules
    limits=[15,20,15,23,33,23]
    i=0
    for sum in sums:
        if sum < limits[i]:
            colors[i] = 'blue'
        elif sum < limits[i+3]:
            colors[i] = 'green'
        else:
            colors[i] = 'red'
        i=i+1

    if sums[0]+sums[1] < 54:
        if colors[0] == 'red':
            colors[0]='green'
        if colors[1] == 'red':
            colors[1]='green'

    render_statistics()
    print('Sum of all subjects: ' + str(sums))
# Statistics text is changed according to the current calculated data
def render_statistics():
    global sums,colors
    i=0
    for number in sums:
       numbers[i]['text']=str(number)
       numbers[i]['foreground']=colors[i]
       i=i+1
