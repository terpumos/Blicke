import matplotlib
import matplotlib.pyplot as plt

font_size=10
fig = plt.figure()
ax = fig.add_subplot(111)

def draw_dyade(x,y,dyads):
	dyade_len=len(dyads)
	rect1 = matplotlib.patches.Rectangle((x*dx,y*dy), dx*dyade_len, dy, facecolor='white',edgecolor='black')
	ax.add_patch(rect1)
	plt.xlim([0,xlen])
	plt.ylim([0,ylen])
	for i in range(dyade_len):
		if(i!=(dyade_len-1)):
			plt.text((x+i)*dx,(y+0.5)*dy,dyads[i]+",",size=font_size)
		else:
			plt.text((x+i)*dx,(y+0.5)*dy,dyads[i],size=font_size)

xlen=400
ylen=400

xtiles=60
ytiles=10

dx=xlen/xtiles
dy=ylen/ytiles

draw_dyade(0,1,["54","42","6"])
draw_dyade(2,4,["56","10","09"])

frame1=plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)

plt.show()

