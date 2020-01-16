import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as m
import numpy as np
import time as t
import random

def translation(p1,p2,angle,d):
    trans_vec = [d*m.cos(angle),d*m.sin(angle)]
    return [p+t for (p,t) in zip(p1,trans_vec)],[p+t for (p,t) in zip(p2,trans_vec)]

def rotor_plot(R1,R2,center,d,h,magnet_point,dl):
    alpha = list(np.linspace(0,2*m.pi,1000))
    x1 = [center[0]+R1*m.cos(alp) for alp in alpha]
    y1 = [center[1]+R1*m.sin(alp) for alp in alpha]
    x2 = [center[0]+R2*m.cos(alp) for alp in alpha]
    y2 = [center[1]+R2*m.sin(alp) for alp in alpha]
    z1 = 1000*[d/2]
    z2 = 1000*[d/2+h]
    z3 = [-z for z in z1]
    z4 = [-z for z in z2]
    fig = plt.figure()
    ax3d = Axes3D(fig)
    ax3d.set_xlabel("X axis")
    ax3d.set_ylabel("Y axis")
    ax3d.set_zlabel("Z axis")
    ax3d.plot([center[0]],[center[1]],[center[2]],'k.')
    #ax3d.set_title("Scatter plot", alpha=0.6, color="b", size=25, weight='bold', backgroundcolor="y")
    ax3d.plot(x1,y1,z1,'gray')
    ax3d.plot(x2,y2,z1,'gray')
    ax3d.plot(x1,y1,z2,'gray')
    ax3d.plot(x2,y2,z2,'gray')
    ax3d.plot(x1,y1,z3,'gray')
    ax3d.plot(x2,y2,z3,'gray')
    ax3d.plot(x1,y1,z4,'gray')
    ax3d.plot(x2,y2,z4,'gray')

    for points in magnet_point:
        ax3d.plot([points[0][0],points[1][0]],[points[0][1],points[1][1]],[points[0][2],points[1][2]],'b-')
        ax3d.plot([points[2][0],points[3][0]],[points[2][1],points[3][1]],[points[2][2],points[3][2]],'b-')
        ax3d.plot([points[4][0],points[5][0]],[points[4][1],points[5][1]],[points[4][2],points[5][2]],'b-')
        ax3d.plot([points[6][0],points[7][0]],[points[6][1],points[7][1]],[points[6][2],points[7][2]],'b-')
        
        ax3d.plot([points[0][0],points[4][0]],[points[0][1],points[4][1]],[points[0][2],points[4][2]],'b-')
        ax3d.plot([points[1][0],points[5][0]],[points[1][1],points[5][1]],[points[1][2],points[5][2]],'b-')
        ax3d.plot([points[2][0],points[6][0]],[points[2][1],points[6][1]],[points[2][2],points[6][2]],'b-')
        ax3d.plot([points[3][0],points[7][0]],[points[3][1],points[7][1]],[points[3][2],points[7][2]],'b-')
        
        th11 = m.atan(points[0][1]/points[0][0]) if points[0][0]>0 else m.atan(points[0][1]/points[0][0])+m.pi
        th21 = m.atan(points[2][1]/points[2][0]) if points[2][0]>0 else m.atan(points[2][1]/points[2][0])+m.pi
        th12 = m.atan(points[1][1]/points[1][0]) if points[1][0]>0 else m.atan(points[1][1]/points[1][0])+m.pi
        th22 = m.atan(points[3][1]/points[3][0]) if points[3][0]>0 else m.atan(points[3][1]/points[3][0])+m.pi

        alpha_1 = list(np.linspace(th11,th21,100))
        alpha_2 = list(np.linspace(th12,th22,100))
        hu1x = [R1*m.cos(alp1) for alp1 in alpha_1]
        hu1y = [R1*m.sin(alp1) for alp1 in alpha_1]
        hu2x = [R2*m.cos(alp2) for alp2 in alpha_2]
        hu2y = [R2*m.sin(alp2) for alp2 in alpha_2]

        ax3d.plot(hu1x,hu1y,z1[0:100],'b-')
        ax3d.plot(hu1x,hu1y,z2[0:100],'b-')
        ax3d.plot(hu2x,hu2y,z1[0:100],'b-')
        ax3d.plot(hu2x,hu2y,z2[0:100],'b-')
        ax3d.plot(hu1x,hu1y,z3[0:100],'b-')
        ax3d.plot(hu1x,hu1y,z4[0:100],'b-')
        ax3d.plot(hu2x,hu2y,z3[0:100],'b-')
        ax3d.plot(hu2x,hu2y,z4[0:100],'b-')

#    for dle in dl:
#        ax3d.plot([0,dle[0]],[0,dle[1]],[z1[0],z1[0]],'k--')
    return ax3d,fig
def find_point(p1,p2,R):
    if abs(p1[0] - p2[0]) < 1e-10:
        y1 = m.sqrt(R**2-p1[0]**2)
        y2 = -y1
        x1 =  p1[0]
        x2 = x1
        if y1 > min(p1[1],p2[1]) and y1 < max(p1[1],p2[1]):
            return [x1,y1]
        else:
            return [x2,y2]
    else:
        k = (p2[1]-p1[1])/(p2[0]-p1[0])
        d = p1[1]-k*p1[0]
        a = k**2+1
        b = 2*k*d
        c = d**2 - R**2
        x1 = (-b+m.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-m.sqrt(b**2-4*a*c))/(2*a)
        y1 = k*x1 + d
        y2 = k*x2 + d
        if x1 > min(p1[0],p2[0]) and x1 < max(p1[0],p2[0]):
            return [x1,y1]
        else:
            return [x2,y2]

def rotor_construction(pn,R1,R2,theta,D,d,h):
    magnet_point = []
    dash_line = []
    z = [D/2,D/2+h]
    for q in range(pn):
        theta_p1 = q*theta
        theta_p2 = theta_p1+theta
        p0 = [0,0]
        p1 = [R2*m.cos(theta_p1),R2*m.sin(theta_p1)]
        p2 = [R2*m.cos(theta_p2),R2*m.sin(theta_p2)]
        
        q1,q2 = translation(p0,p1,m.pi/2+theta_p1,d)
        q3,q4 = translation(p0,p2,m.pi/2+theta_p2,-d)
        
        q1_ = find_point(q1,q2,R1)
        q2_ = find_point(q1,q2,R2)
        q3_ = find_point(q3,q4,R1)
        q4_ = find_point(q3,q4,R2)
        
        alpha_1 = [theta_p1 + m.asin(d/R) for R in [R1,R2]]
        alpha_2 = [theta_p2 - m.asin(d/R) for R in [R1,R2]]
        
        alpha = [alpha_1,alpha_2]
        dash_line.append(p1)
        magnet_point.append([q1_+[z[0]],q2_+[z[0]],q3_+[z[0]],q4_+[z[0]],q1_+[z[1]],q2_+[z[1]],q3_+[z[1]],q4_+[z[1]],alpha])
        magnet_point.append([q1_+[-z[1]],q2_+[-z[1]],q3_+[-z[1]],q4_+[-z[1]],q1_+[-z[0]],q2_+[-z[0]],q3_+[-z[0]],q4_+[-z[0]],alpha])
    return magnet_point,dash_line

def if_in(point,magnet,R1,R2):
    def theta_(r,P,Q):
        r0 = [(q-p)*(r-R1)/(R2-R1)+p for (p,q) in zip(P,Q)]
        return m.atan(r0[1]/r0[0]) if r0[0]>0 else m.atan(r0[1]/r0[0])+m.pi
    z1 = magnet[0][2]
    z2 = magnet[4][2]
    z = point[2]
    R = m.sqrt((point[0])**2+(point[1])**2)
    th = m.atan(point[1]/point[0])
    theta = th if point[0]>0 else th+m.pi
    if z<=z2 and z>=z1:
        if R <=R2 and R>=R1:
            theta1 = theta_(R,magnet[2],magnet[3])
            theta2 = theta_(R,magnet[0],magnet[1])
            if theta<=theta1  and theta>=theta2:
                if abs(z-z1)<1e-10 or abs(z-z2)<1e-10 or abs(R-R1)<1e-10 or abs(R-R2)<1e-10 or abs(theta-theta1)<1e-10 or abs(theta-theta2)<1e-10:
                    return 0
                else:
                    return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1

def if_in_all(p,magnet_point,R1,R2):
    IFIN = -1
    for magnet in magnet_point:
        if if_in(p,magnet,R1,R2)==1:
            IFIN = 1
            break
        elif if_in(p,magnet,R1,R2)==0:
            IFIN = 0
            break
    return IFIN

def test_theta_(magnet_point,R1,R2):
#    test theta_()
    R = list(np.linspace(R1,R2,100))
    th = [theta_(r,magnet_point[4][0],magnet_point[4][1],R1,R2) for r in R]
    x = [r*m.cos(t) for (r,t) in zip(R,th)]
    y = [r*m.sin(t) for (r,t) in zip(R,th)]
    z = delta_D/2+magnet_h
    plt.plot(x,y,z,'o-')


def test_if_in1(ax3d,magnet_point,R1,R2):
#    test if_in() #1
    X = list(np.linspace(-9,9,20))
    Y = X
    Z = list(np.linspace(-3,3,20))
    P1=[[],[],[]]
    P2=[[],[],[]]
    P3=[[],[],[]]
    for x in X:
        for y  in Y:
            for z in Z:
                IFIN = if_in_all([x,y,z],magnet_point,R1,R2)
                if IFIN==1:
                    P1[0].append(x)
                    P1[1].append(y)
                    P1[2].append(z)
                elif IFIN==0:
                    P2[0].append(x)
                    P2[1].append(y)
                    P2[2].append(z)
                else:
                    P3[0].append(x)
                    P3[1].append(y)
                    P3[2].append(z)
                    
    ax3d.plot(P1[0],P1[1],P1[2],'r.',alpha=1)
    ax3d.plot(P2[0],P2[1],P2[2],'g.',alpha=0.5)
    ax3d.plot(P3[0],P3[1],P3[2],'y.',alpha=0.25)

def test_if_in2(ax3d,magnet_point,R1,R2):
#    test if_in() #2
    P1=[[],[],[]]
    P2=[[],[],[]]
    P3=[[],[],[]]
    for i in range(5000):
        x = 18*random.random()-9
        y = 18*random.random()-9
        z = 6*random.random()-3
        IFIN = if_in_all([x,y,z],magnet_point,R1,R2)
        if IFIN==1:
            P1[0].append(x)
            P1[1].append(y)
            P1[2].append(z)
        elif IFIN==0:
            P2[0].append(x)
            P2[1].append(y)
            P2[2].append(z)
        else:
            P3[0].append(x)
            P3[1].append(y)
            P3[2].append(z)
            
    for z in [-delta_D/2-magnet_h,-delta_D/2,delta_D/2,delta_D/2+magnet_h]:
        for i in range(100):
            x = 18*random.random()-9
            y = 18*random.random()-9
            IFIN = if_in_all([x,y,z],magnet_point,R1,R2)
            if IFIN==1:
                P1[0].append(x)
                P1[1].append(y)
                P1[2].append(z)
            elif IFIN==0:
                P2[0].append(x)
                P2[1].append(y)
                P2[2].append(z)
            else:
                P3[0].append(x)
                P3[1].append(y)
                P3[2].append(z)
    for r in [R1,R2]:
        for i in range(500):
            al = 2*m.pi*random.random()
            x = r*m.cos(al)
            y = r*m.sin(al)
            z = 6*random.random()-3
            IFIN = if_in_all([x,y,z],magnet_point,R1,R2)
            if IFIN==1:
                P1[0].append(x)
                P1[1].append(y)
                P1[2].append(z)
            elif IFIN==0:
                P2[0].append(x)
                P2[1].append(y)
                P2[2].append(z)
            else:
                P3[0].append(x)
                P3[1].append(y)
                P3[2].append(z)
    ax3d.plot(P1[0],P1[1],P1[2],'r.',alpha=1)
    ax3d.plot(P2[0],P2[1],P2[2],'g.',alpha=0.5)
    ax3d.plot(P3[0],P3[1],P3[2],'y.',alpha=0.25)


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

magnet_point,dash_line = rotor_construction(pn,R1,R2,p_theta,delta_D,d,magnet_h)
ax3d,fig = rotor_plot(R1,R2,[0,0,0],delta_D,magnet_h,magnet_point,dash_line)
#test_if_in2(ax3d,magnet_point,R1,R2)
plt.show()
