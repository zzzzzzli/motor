import math as m
import numpy as np
import make_rotor as mr

def fea(nodes,units,magnets,R1,R2,mu_in,mu_out,test):
    K = []
    Nnode = len(node)
    K = Nnode*[Nnode*[0.]]
    mu = Node*[0.]
    P = Node*[0.]
    for unit in units:
        x = [nodes[n][0] for n in unit]
        y = [nodes[n][1] for n in unit]
        z = [nodes[n][2] for n in unit]
        A = np.([[1,x[0],y[0],z[0]],[1,x[1],y[1],z[1]],[1,x[2],y[2],z[2]],[1,x[3],y[3],z[3]]])
        V = np.linalg.det(A)
        a_m[0] = [[x[1],y[1],z[1]],[x[2],y[2],z[2]],[x[3],y[3],z[3]]]
        a_m[1] = [[x[0],y[0],z[0]],[x[2],y[2],z[2]],[x[3],y[3],z[3]]]
        a_m[2] = [[x[0],y[0],z[0]],[x[1],y[1],z[1]],[x[3],y[3],z[3]]]
        a_m[3] = [[x[0],y[0],z[0]],[x[1],y[1],z[1]],[x[2],y[2],z[2]]]
        
        b_m[0] = [[1,y[1],z[1]],[1,y[2],z[2]],[1,y[3],z[3]]]
        b_m[1] = [[1,y[0],z[0]],[1,y[2],z[2]],[1,y[3],z[3]]]
        b_m[2] = [[1,y[0],z[0]],[1,y[1],z[1]],[1,y[3],z[3]]]
        b_m[3] = [[1,y[0],z[0]],[1,y[1],z[1]],[1,y[2],z[2]]]
        
        c_m[0] = [[x[1],1,z[1]],[x[2],1,z[2]],[x[3],1,z[3]]]
        c_m[1] = [[x[0],1,z[0]],[x[2],1,z[2]],[x[3],1,z[3]]]
        c_m[2] = [[x[0],1,z[0]],[x[1],1,z[1]],[x[3],1,z[3]]]
        c_m[3] = [[x[0],1,z[0]],[x[1],1,z[1]],[x[2],1,z[2]]]
        
        d_m[0] = [[x[1],y[1],1],[x[2],y[2],1],[x[3],y[3],1]]
        d_m[1] = [[x[0],y[0],1],[x[2],y[2],1],[x[3],y[3],1]]
        d_m[2] = [[x[0],y[0],1],[x[1],y[1],1],[x[3],y[3],1]]
        d_m[3] = [[x[0],y[0],1],[x[1],y[1],1],[x[2],y[2],1]]
        
        a = np.linalg.det(a_m)/6
        b = -np.linalg.det(b_m)/6
        c = np.linalg.det(c_m)/6
        d = -np.linalg.det(d_m)/6
        
        N = len(unit)
        for j in range(N):
            m = unit[j]
            if mu[m]:
                pass
            else:
                if test:
                    IFIN = -1
                    if (magnets[0][0]<node[m][0] and node[m][0]<magnets[1][0]):
                        if (magnets[0][1]<node[m][1] and node[m][1]<magnets[3][1]):
                            if (magnets[4][2]<node[m][2] and node[m][2]<magnets[4][2]):
                                IFIN = 1
                else:
                    IFIN = mr.if_in_all(nodes[m],magnets,R1,R2)
                if IFIN==1:
                    mu[m] = mu_in
                elif IFIN==-1:
                    mu[m] = mu_out
                else:   
                    mu[m] = (mu_in+mu_out)/2
            for i in range(N)
                n = unit[i]
                K[m][n] = K[m][n] + mu[m]*(b[i]*b[j]+c[i]*c[j]+d[i]*d[j])
            if test:
                pass
            else:
                P[m] = a[j]*(magnets[0][0]-magnets[1][0])*(magnets[0][1]-magnets[3][1])*(magnets[4][2]-magnets[4][2])+0.5*(magnets[0][0]-magnets[1][0])*(magnets[0][1]-magnets[3][1])*(magnets[4][2]-magnets[4][2])*(magnets[0][0]+magnets[1][0])+0.5*(magnets[0][0]-magnets[1][0])*(magnets[0][1]-magnets[3][1])*(magnets[4][2]-magnets[4][2])*(magnets[0][1]+magnets[3][1])+0.5*(magnets[0][0]-magnets[1][0])*(magnets[0][1]-magnets[3][1])*(magnets[4][2]-magnets[4][2])*(magnets[4][2]+magnets[4][2])

        