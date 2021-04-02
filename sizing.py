import numpy as np

x = []
y = []
z = []

for i in range(1,80):
    x.append(i)
x = np.array(x)

for j in range(1,33):
    y.append(j)
y = np.array(y)

for k in range(1,61):
    z.append(k)
z = np.array(z)

mesh = np.ones((72,144))


file1 = open(r"C:\Users\smccarthy\Desktop\Workspace\sizes.txt","w+")
for x_dim in x:
    for y_dim in y:
        for z_dim in z:
            area = x_dim*y_dim + 2*z_dim*y_dim + 2*x_dim*z_dim #Base * Sides * Front & Back
            volume = x_dim*y_dim*z_dim
            if area < 72*144 and volume > 75000:
                wall = (z_dim,y_dim)    #Create rectangles, length and height
                base = (x_dim,y_dim)
                back = (x_dim,z_dim)
                basket = [wall, wall, base, back, back] #store into array
                basket.sort()
                remaining_mesh = mesh
                open_space_x = 0
                open_space_y = 0
                for rectangle in basket:
                    if sum(remaining_mesh[0:-1][0]) > rectangle[0] and sum(remaining_mesh[0][0:-1]) > rectangle[1]:
                        remaining_mesh[open_space_x:open_space_x+rectangle[0]][open_space_y:open_space_y+rectangle[1]] = 0
                    #check if width fits
                        #if so, place rectanlge and subtract from mesh
                    #check if width fitss
                    #check if height fits
                        #if so, place rectanlge and subtract from mesh
                    #save and write if it all fits
                    pass
file1.close()