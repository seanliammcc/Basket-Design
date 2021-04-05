import numpy as np

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_height(self):
        return self.y

    def get_width(self):
        return self.x

    def __gt__(self, other):
        self_mag = self.x*self.y
        other_mag = other.get_height() * other.get_width()
        return self_mag < other_mag

    def __str__(self):
        return "("+str(self.x)+', '+str(self.y)+')'


class Bin():
    def __init__(self):
        self.items = []
        self.x = 144
        self.y = 72
        self.mesh = np.ones([self.x, self.y], dtype=int)

    def insert_item(self, item):
        self.items.append(item)

    def modify_mesh(self, height, width,i,j):
        for k in range(i, i + width):
            for l in range(j, j + height):
                self.mesh[k][l] = 0


    def fit_rectangle(self, rectangle: Rectangle):
        height = rectangle.get_height()
        width = rectangle.get_width()
        for i in range(0,self.x - width + 1):
            for j in range(0, self.y - height + 1):
                if self.mesh[i,j] == 1 and self.mesh[i:i+height][j:j+width].all() == 1:
                    self.modify_mesh(height, width, i,j)
                    self.insert_item(rectangle)
                    return True
        return False

    
    def __str__(self):
        return str(self.mesh)

def main_2():
    
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

    #file1 = open("/Users/seanliam/Documents/Air-Tec/sizes.txt","w+")
    file1 = open(r"C:\Users\smccarthy\Desktop\Workspace\sizes.txt","w+")
    # max_vol = -10
    # max_x = 0
    # max_y = 0
    # max_z = 0
    for x_dim in x:
        for y_dim in y:
            for z_dim in z:
                area = x_dim*y_dim + 2*z_dim*y_dim + 2*x_dim*z_dim #Base * Sides * Front & Back
                volume = x_dim*y_dim*z_dim
                if area < 72*144 and volume > 80000:
                    wall = Rectangle(z_dim,y_dim)    #Create rectangles, length and height
                    base = Rectangle(x_dim,y_dim)
                    back = Rectangle(x_dim,z_dim)
                    basket = [wall, wall, base, back, back] #store into array
                    #basket = [wall, wall]
                    basket.sort(reverse=False)
                    mesh = Bin()
                    flag = True
                    for rectangle in basket:
                        if not(mesh.fit_rectangle(rectangle)):
                            flag = False
                            break
                    if flag:
                        # cur_vol = x_dim * y_dim*z_dim
                        file1.write("("+str(x_dim)+', '+str(y_dim)+', '+str(z_dim)+')\n')
                        # if max_vol < cur_vol:
                        #     max_vol = cur_vol
                        #     max_x = x_dim
                        #     max_y = y_dim
                        #     max_z = z_dim

    # print("("+str(max_x)+', '+str(max_y)+', '+str(max_z)+')')
    file1.close()    

def main():
    file1 = open(r"C:\Users\smccarthy\Desktop\Workspace\sizes.txt","r")     
    # file2 = open("/Users/seanliam/Documents/Air-Tec/sizes2.txt","r")
    file2 = open(r"C:\Users\smccarthy\Desktop\Workspace\sizes2.txt","r")
    file3 = open(r"C:\Users\smccarthy\Desktop\Workspace\\allsizes.txt","w+")

    fl1 = file1.readlines()
    fl2 = file2.readlines()
    for line in fl1:
        dims = eval(line)
        vol = dims[0] * dims[1] * dims[2]
        file3.write(str(vol) + ' - ' + line)
    for line in fl2:
        dims = eval(line)
        vol = dims[0] * dims[1] * dims[2]
        file3.write(str(vol) + ' - ' + line)

    file1.close()
    file2.close()
    file3.close()


if __name__ == "__main__":
    main()

