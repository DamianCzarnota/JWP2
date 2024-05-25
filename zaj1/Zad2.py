from math import sqrt

class Vector3D:

    def __init__(self,x:int = 0,y:int = 0,z:int = 0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f"Vector3D({self.__x},{self.__y},{self.__z})"

    def set_x(self,x=0):
        self.__x = x
    def get_x(self) -> int:
        return self.__x

    def set_y(self, x:int =0):
        self.__y = x

    def get_y(self) -> int:
        return self.__y
    def set_z(self,x=0):
        self.__z = x
    def get_z(self) -> int:
        return self.__z

    def norm(self):
        return sqrt(self.__x^2+self.__y^2+self.__z^2)

    def __add__(self, other):
        if isinstance(other, Vector3D):
            self.__x += other.get_x()
            self.__y += other.get_y()
            self.__z += other.get_z()
            return self
        raise RuntimeError("cannot add vector with anything else than vector!")

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            self.__x -= other.get_x()
            self.__y -= other.get_y()
            self.__z -= other.get_z()
            return self
        raise RuntimeError("cannot substract vector with anything else than vector!")


    def __mul__(self, number):
        if isinstance(number,int) or isinstance(number,float):
            self.__x *= number
            self.__y *= number
            self.__z *= number
            return self
        raise RuntimeError("cannot multiply vector with anything else than number!")

    def dot(self,other):
        if isinstance(other, Vector3D):
            return self.__x*other.get_x() + self.__y*other.get_y() + self.__z * other.get_z()
        raise RuntimeError("other is not a Vector3D!")


    def cross(self,other):
        if isinstance(other, Vector3D):
            return Vector3D(
                self.__y*other.get_z() - self.__z*other.get_y(),
                self.__z*other.get_x() - self.__x*other.get_z(),
                self.__x*other.get_y() - self.__y*other.get_x()
            )
        raise RuntimeError("other is not a Vector3D!")

    @staticmethod
    def are_orthogonal(vector_1,vector_2):
        if isinstance(vector_1,Vector3D) and isinstance(vector_2,Vector3D):
            return vector_1.dot(vector_2) == 0



if __name__ == "__main__":

    print("To jest main")

    v1 = Vector3D()
    v0 = Vector3D()
    v0_2 = Vector3D()
    v2 = Vector3D(5,3,2)
    v3 = Vector3D(1,6,2)

    print(v1)
    v1 += v2
    print(v1)
    v1 -= v3
    print(v1)

    print(v1)

    print(v1*2)

    print(v1.dot(v3))
    print(v1.cross(v2))
    print(v0.cross(v0_2))

    print(Vector3D.are_orthogonal(v0,v3))

