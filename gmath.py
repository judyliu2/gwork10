import math
from matrix import*
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normal = normalize(normal)
    view = normalize(view)
    light[LOCATION] = normalize(light[LOCATION])

    a = calculate_ambient(ambient, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)

    i = [0,0,0]
    i[0] = a[0] + d[0] + s[0]
    i[1] = a[1] + d[1] + s[1]
    i[2] = a[2] + d[2] + s[2]
    limit_color(i)
    return i
        
    

#each should return [r,g,b]
def calculate_ambient(alight, areflect):
    a = [0,0,0]
    a[0] = alight[0] * areflect[0]
    a[1] = alight[1] * areflect[1]
    a[2] = alight[2] * areflect[2]

    return a
        

def calculate_diffuse(light, dreflect, normal):
    d = [0,0,0]
    d[0] = light[COLOR][0] * dreflect[0] * dot_product(light[LOCATION], normal)
    d[1] = light[COLOR][1] * dreflect[1] * dot_product(light[LOCATION], normal)
    d[2] = light[COLOR][2] * dreflect[2] * dot_product(light[LOCATION], normal)
    return d
    

def calculate_specular(light, sreflect, view, normal):
    s = [0,0,0]
    dp1 = 2 * dot_product(normal, light[LOCATION])
    r = [0,0,0]
    r[0] = normal[0]*dp1 - light[LOCATION][0]
    r[1] = normal[1]*dp1 - light[LOCATION][1]
    r[2] = normal[2]*dp1 - light[LOCATION][2]
    
    dp2 = dot_product(r, view)
    if( dp2< 0):
        dp2 = 0
    

    s[0] = light[COLOR][0] * sreflect[0] * (dp2 ** SPECULAR_EXP)
    s[1] = light[COLOR][1] * sreflect[1] * (dp2 ** SPECULAR_EXP)
    s[2] = light[COLOR][2] * sreflect[2] * (dp2 ** SPECULAR_EXP)

    return s
 

def limit_color(color):
    for x in range(0,3):
        if (color[x] > 255):
            color[x] = 255
        elif (color[x]<0):
            color[x] = 0

#vector functions
def normalize(vector):
    magnitude = (vector[0]**2 + vector[1]**2 + vector[2]**2) **0.5
    vector[0] = vector[0]/magnitude
    vector[1] = vector[1]/magnitude
    vector[2] = vector[2]/magnitude
    return vector


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
