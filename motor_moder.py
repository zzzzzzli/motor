import matplotlib.pyplot as plt
import math as m
import numpy as np

def translation(p1,p2,angle,d):
    trans_vec = [d*m.cos(angle),d*m.sin(angle)]
    print(p1)
    print(p2)
    print(p1+trans_vec)
    print(p2+trans_vec)
    return [p+t for (p,t) in zip(p1,trans_vec)],[p+t for (p,t) in zip(p2,trans_vec)]

def plot_circle(R1,R2,center):
    alpha = list(np.linspace(0,2*m.pi,100))
    x1 = [center[0]+R1*m.cos(alp) for alp in alpha]
    y1 = [center[1]+R1*m.sin(alp) for alp in alpha]
    x2 = [center[0]+R2*m.cos(alp) for alp in alpha]
    y2 = [center[1]+R2*m.sin(alp) for alp in alpha]
    plt.plot(x1,y1,'g-',x2,y2,'g-')
    plt.plot(center,'.')

def rotor_construction(R1,R2,theta,D,d,h):
    magnet_line = []
    for q in range(pn):
        theta_p1 = q*theta
        theta_p2 = theta_p1+theta
        p0 = [0,0]
        p1 = [R2*m.cos(theta_p1),R2*m.sin(theta_p1)]
        p2 = [R2*m.cos(theta_p2),R2*m.sin(theta_p2)]
        plt.plot([p0[0],p1[0]],[p0[1],p1[1]],'k--')
        q1,q2 = translation(p0,p1,m.pi/2+theta_p1,d)
        q3,q4 = translation(p0,p2,m.pi/2+theta_p2,-d)
        magnet_line.append([[q1,q2],[q3,q4]])
    print('气隙宽度：'+str(D)+'mm')
    print('磁铁厚度：'+str(h)+'mm')
    print('磁铁间距：'+str(2*d)+'mm')
    z = [D/2,D/2+h]
    return magnet_line,z
 


pn = 12
p_theta = 2*m.pi/pn;
d = 1
R1 = 10
R2 = R1*m.sqrt(3)
delta_D=5
magnet_h=10


plot_circle(R1,R2,[0,0])
magnet_line,z = rotor_construction(R1,R2,p_theta,delta_D,d,magnet_h)
for line_pair in magnet_line:
    plt.plot([line_pair[0][0][0],line_pair[0][1][0]],[line_pair[0][0][1],line_pair[0][1][1]],'b-',[line_pair[1][0][0],line_pair[1][1][0]],[line_pair[1][0][1],line_pair[1][1][1]],'b-')


plt.axis('equal')
plt.show()
