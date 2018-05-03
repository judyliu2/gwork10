import math
from matrix import *
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    return limit_color(calculate_ambient(ambient, areflect) +
    calculate_diffuse(light, dreflect, normal) +
    calculate_specular(light, sreflect, view, normal))

#each should return [r,g,b]
def calculate_ambient(alight, areflect):
    return alight * areflect

def calculate_diffuse(light, dreflect, normal):
    DIFFUSE * dreflect * dot_product(normalize(light), normal)

def calculate_specular(light, sreflect, view, normal):
    SPECULAR * sreflect * ( dot_product(
        2 * dot_product(normal, normalize(light)) *
        normal - light), view) ** SPECULAR_EXP 

def limit_color(color):
    i = 0
    while (i < len(color)): 
        if (color <= 255 and color >= 0):
            return
        else:
            color = 0
        i+=1

#vector functions
def normalize(vector):
    magnitude = sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    vector[0] = int(vector[0]/magnitude)
    vector[1] = int(vector[1]/magnitude)
    vector[2] = int(vector[2]/magnitude)


def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
