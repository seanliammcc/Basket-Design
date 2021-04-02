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
        self.x = 10
        self.y = 10
        self.mesh = np.ones([self.x, self.y], dtype=int)

    def insert_item(self, item):
        self.items.append(item)

    # def find_first(self, lateral):
    #     if lateral:
    #         end = self.x
    #     else:
    #         end = self.y
    #     for k in range(0,end):
    #         if self.mesh[k] == 1:
    #             return k

    def modify_mesh(self, height, width,i,j):
        for k in range(i, i + width):
            for l in range(j, j + height):
                self.mesh[k][l] = 0


    def fit_rectangle(self, rectangle: Rectangle):
        height = rectangle.get_height()
        width = rectangle.get_width()
        print(height, width)
        for i in range(0,self.x - width + 1):
            for j in range(0, self.y - height + 1):
                if self.mesh[i,j] == 1 and self.mesh[i:i+height][j:j+width].all() == 1:
                    self.modify_mesh(height, width, i,j)
                    self.insert_item(rectangle)
                    return True
        return False

    
    def __str__(self):
        return str(self.mesh)

def main():
    
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

    file1 = open(r"C:\Users\smccarthy\Desktop\Workspace\sizes.txt","w+")


    for x_dim in x:
        for y_dim in y:
            for z_dim in z:
                area = x_dim*y_dim + 2*z_dim*y_dim + 2*x_dim*z_dim #Base * Sides * Front & Back
                volume = x_dim*y_dim*z_dim
                if area < 72*144 and volume > 75000:
                    wall = Rectangle(z_dim,y_dim)    #Create rectangles, length and height
                    base = Rectangle(x_dim,y_dim)
                    back = Rectangle(x_dim,z_dim)
                    basket = [wall, wall, base, back, back] #store into array
                    # basket = [wall, wall]
                    basket.sort(reverse=False)
                    mesh = Bin()
                    for rectangle in basket:
                        if mesh.fit_rectangle(rectangle):
                            pass

    file1.close()         


# if __name__ == "__main__":
#     main()

