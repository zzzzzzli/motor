import numpy as np


def cubics_space(xmin,xmax,nx,ymin,ymax,ny,zmin,zmax,nz):
    def n(i,j,k):
        return k*nx*ny+j*nx+i
    grid_X = list(np.linspace(xmin,xmax,nx))
    grid_Y = list(np.linspace(ymin,ymax,ny))
    grid_Z = list(np.linspace(zmin,zmax,nz))
    position =  nx*ny*nz*[[0,0,0]]
    cubics = []
    for z in grid_Z:
        for y in grid_Y:
            for x in grid_X:
                i = grid_X.index(x)
                j = grid_Y.index(y)
                k = grid_Z.index(z)
                position[n(i,j,k)] = [x,y,z]
                if i!=nx-1 and j!=ny-1 and k!=nz-1:
                    cubics.append([n(i,j,k),n(i+1,j,k),n(i,j+1,k),n(i+1,j+1,k),n(i,j,k+1),n(i+1,j,k+1),n(i,j+1,k+1),n(i+1,j+1,k+1)])
    return position,cubics
    
def tetrahedron_space(cubics):
    tetrahedron = []
    for cubic in cubics:
        tetrahedron.append([cubic[0],cubic[1],cubic[2],cubic[4]])
        tetrahedron.append([cubic[3],cubic[1],cubic[2],cubic[7]])
        tetrahedron.append([cubic[5],cubic[1],cubic[4],cubic[7]])
        tetrahedron.append([cubic[6],cubic[4],cubic[2],cubic[7]])
    return tetrahedron
    
def cubic_space_plot(ax3d,position,cubics):
    ax3d.set_xlabel("X axis")
    ax3d.set_ylabel("Y axis")
    ax3d.set_zlabel("Z axis")
    for p in position:
        ax3d.plot([p[0]],[p[1]],[p[2]],'k.')
    for cub in cubics:
        for i in [0,2,4,6]:
            j = cub[i]
            k = cub[i+1]
            ax3d.plot([position[j][0],position[k][0]],[position[j][1],position[k][1]],[position[j][2],position[k][2]],'r-')
        for i in [0,1,2,3]:
            j = cub[i]
            k = cub[i+4]
            ax3d.plot([position[j][0],position[k][0]],[position[j][1],position[k][1]],[position[j][2],position[k][2]],'g-')
        for i in [0,1,4,5]:
            j = cub[i]
            k = cub[i+2]
            ax3d.plot([position[j][0],position[k][0]],[position[j][1],position[k][1]],[position[j][2],position[k][2]],'b-')
            
def tetrahedron_space_plot(ax3d,position,tetrahedron):
    ax3d.set_xlabel("X axis")
    ax3d.set_ylabel("Y axis")
    ax3d.set_zlabel("Z axis")
    for p in position:
        ax3d.plot([p[0]],[p[1]],[p[2]],'k.')
    Ntet = len(tetrahedron)
    d_tou = 1/Ntet
    toumingdu = 1
    for tet in tetrahedron[3::4]:
        toumingdu = toumingdu - d_tou
        for ij in [[tet[0],tet[1]],[tet[0],tet[2]],[tet[0],tet[3]],[tet[1],tet[2]],[tet[1],tet[3]],[tet[2],tet[3]]]:
            i,j = ij
            ax3d.plot([position[i][0],position[j][0]],[position[i][1],position[j][1]],[position[i][2],position[j][2]],'b-',alpha=toumingdu)