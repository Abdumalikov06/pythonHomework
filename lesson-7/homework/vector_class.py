import math
class Vector:
    def __init__(self,*args):
        self.args=args

    def get_dimensions(self):
       return self.args
    def __str__(self):
        return " ".join(map(str, self.args))
    def __add__(self, other):
        result=[]
        try:
            for v1,v2 in zip(self.args, other.args):
                result.append(v1+v2)
            return Vector(*result)
        except ValueError:
            print("Vectors should have same dimensions")
    #subtraction of vectors
    def __sub__(self,other):
        try:
            result=[]
            for v1,v2 in zip(self.args,other.args):
                if v1>=v2:
                    result.append(v1-v2)
                elif v2>v1:
                    result.append(v2-v1)
            return Vector(*result)
        except ValueError:
            print("Vectors should have same dimensions")
    #Multiplying two vectors
    def __mul__(self,other):
        try:
            if isinstance(other, (int, float)):  # Scalar multiplication
                result = [args * other for args in self.args]
                return Vector(*result)
            else:
                result=[]
                for v1,v2 in zip(self.args,other.args):
                    result.append(v1*v2)
                sum_result=sum(result)
                return sum_result
        except (ValueError, AttributeError):
            print("Vectors should have same dimensions") 
    def __rmul__(self,other):
        #this function works when the scalar is on the right side and vector is on the left
        try:
            if isinstance(other, (int,float)):
                result=[args*other for args in self.args]
            return Vector(*result)
        except (ValueError,AttributeError):
            print("''other must be scalar")
    def magnitude(self):
        return math.sqrt(sum(args**2 for args in self.args))
    def normalize(self):
        #normalizing is dividing each vector by magnitude 
        #round them by 3 decimals and used math library to calculate magnitude
         result=[round(args/(math.sqrt(sum(args**2 for args in self.args))),3) for args in self.args]
         return Vector(*result)
          

    




v1 = Vector(1, 2, 3)
v2=Vector(4,5,6)
v3=v1+v2
v4=v2-v1
dot_product=v1*v2
v5=3*v1
print(f"v1 is: {v1}")
print(f"v2 is: {v2}")
print(f"sum of vectors: {v3}")
print(f"substraction of vectors: {v4}")
print(f"sum of product of vectors: {dot_product}")
print(f"scalar multiplication of v1 is {v5}")
print(f"magnitude of v1 vector is: {v1.magnitude()}")
print(f"normalized v1 vector is: {v1.normalize()}")
        