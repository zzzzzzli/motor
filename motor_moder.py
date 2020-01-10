import matplotlib.pyplot as plt
import math as m
import numpy as np

def translation(p1,p2,angle,d):
    trans_vec = [d*m.cos(angle),d*m.sin(angle)]
    return [p+t for (p,t) in zip(p1,trans_vec)],[p+t for (p,t) in zip(p2,trans_vec)]

def plot_circle(R1,R2,center):
    alpha = list(np.linspace(0,2*m.pi,100))
    x1 = [center[0]+R1*m.cos(alp) for alp in alpha]
    y1 = [center[1]+R1*m.sin(alp) for alp in alpha]
    x2 = [center[0]+R2*m.cos(alp) for alp in alpha]
    y2 = [center[1]+R2*m.sin(alp) for alp in alpha]
    plt.plot(x1,y1,'g-',x2,y2,'g-')
    plt.plot(center[0],center[1],'.')
    
def find_point(p1,p2,R):
    if p1[1] \= p2[1]:
        k = (p2[1]-p1[1])/(p2[0]-p1[0])
        d = p1[1]-k*p1[0]
        a = k*k+1
        b = 2*k*d
        c = d*d - R*R
        x1 = (m.sqrt(b*b-4*a*c)+b)/(2*a)
        x2 = (m.sqrt(b*b-4*a*c)-b)/(2*a)
        y1 = k*x1 + d
        y2 = k*x2 + d
    else:
        x1 = m.sqrt(R**2-p1[1]**2)
        x2 = -x1
        y1 =  p1[1]
        y2 = y1
    
    return [x,y]

def rotor_construction(pn,R1,R2,theta,D,d,h):
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
        q1 = find_point(q1,q2,R1)
        q2 = find_point(q1,q2,R2)
        q3 = find_point(q1,q2,R1)
        q4 = find_point(q1,q2,R2)        
    for line_pair in magnet_line:
        plt.plot([q1[0],q2[0]],[q1[1],q2[1]],'b-',[q3[0],q4[0]],[q3[1],q4[1]],'b-')
    z = [D/2,D/2+h]
    #return magnet_line,z
 


pn = 6
p_theta = 2*m.pi/pn;
d = 1
R1 = 10
R2 = 17#R1*m.sqrt(3)
delta_D=5
magnet_h=2

print('转子内径：'+str(R1)+'mm')
print('转子外径：'+str(R2)+'mm')
print('气隙宽度：'+str(delta_D)+'mm')
print('磁铁厚度：'+str(magnet_h)+'mm')
print('磁铁间距：'+str(2*d)+'mm')


plot_circle(R1,R2,[0,0])
rotor_construction(pn,R1,R2,p_theta,delta_D,d,magnet_h)



plt.axis('equal')
plt.show()
