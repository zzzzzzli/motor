import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import grid_space as gs
import make_rotor as mr

pn = 4
p_theta = 2*m.pi/pn;
d = 1
R1 = 5
R2 = 8#R1*m.sqrt(3)
delta_D=1
magnet_h=1.5

print('磁极内径：'+str(R1)+'mm')
print('磁极外径：'+str(R2)+'mm')
print('气隙宽度：'+str(delta_D)+'mm')
print('磁极厚度：'+str(magnet_h)+'mm')
print('磁极间距：'+str(2*d)+'mm')

fig = plt.figure()
ax3d = Axes3D(fig)

#magnet_point,dash_line = mr.rotor_construction(pn,R1,R2,p_theta,delta_D,d,magnet_h)
#mr.rotor_plot(ax3d,R1,R2,[0,0,0],delta_D,magnet_h,magnet_point,dash_line)
#mr.test_if_in2(ax3d,magnet_point,R1,R2,delta_D,magnet_h)
position,element = gs.cubic_space(-5,5,4,-5,5,4,-5,5,4)
gs.space_plot(ax3d,position,element)




plt.show()