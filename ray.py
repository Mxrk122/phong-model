import math
from render import Render
import color
from vector3 import V3
from sphere import Sphere
from light import Light

class Raytracer(object):
    def __init__(self, filename, width, height):
        self.filename = filename
        self.width = width
        self.height = height
        self.clear_color = color.color_RGB_to_GBR(0, 0, 0)
        self.paint_color = color.color_RGB_to_GBR(1, 1, 1)
        self.framebuffer = [[]]
        self.scene = []
        self.light = None
        self.clear()

    def change_paint_color(self, r, g, b):
        self.paint_color = color.color_RGB_to_GBR(r, g, b)
    
    def change_clear_color(self, r, g, b):
        self.clear_color = color.color_RGB_to_GBR(r, g, b)
    
    def set_light(self, position: V3, intensity, color):
        self.light = Light(position, intensity,  color)

    def point(self, x, y, c = None):
        if (y >= 0 and y < self.height) and (x >= 0 and x < self.width):
            self.framebuffer[y][x] = c or self.paint_color

    # funcion para pintar todo el mapa de bits de un color
    def clear(self):
        self.framebuffer = [
            # for para rellenar el array -> generador
            # se pinta del color que indique clear_color
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self):
        r = Render()
        r.write(self.filename + ".bmp", self.width, self.height, self.framebuffer)

    def render(self):
        fov = int(math.pi/2)
        ar = self.width/self.height

        for y in range(self.height):
            for x in range(self.width):
                i = ((2 * (x + 0.5) / self.width) - 1) * math.tan(fov/2) * ar
                j = ( 1 - (2 * (y + 0.5) / self.height)) * math.tan(fov/2) * ar

                direction = V3(i, j, -1).normalize()
                origin = V3(0, 0, 0)

                c = self.cast_ray(origin, direction)

                self.point(x, y, c)
    
    def addSphere(self, center: V3, radius, material):
        self.scene.append(Sphere(center, radius, material))
    
    #Método para calcular la reflexión.
    def reflect(self, I, N):
        return (I - (N * 2 * (N @ I))).normalize()
    
    def scene_intersect(self, origin, direction):
        zBuffer = 999999

        material = None

        intersect = None

        for o in self.scene:
            obj_intersect = o.ray_intersect(origin, direction)
            
            if obj_intersect:
                if obj_intersect.distance < zBuffer:
                    zBuffer = obj_intersect.distance
                    material = o.material
                    intersect = obj_intersect
                    
        return material, intersect

    def cast_ray(self, origin, direction):
        material, intersect  = self.scene_intersect(origin, direction)

        if material == None:
            return self.clear_color
        
        # direccion de la luz

        light_direction = (self.light.position - intersect.point).normalize()

        # Diffuse component
        diffuse_intensity = light_direction @ intersect.normal

        diffuse = (
            material.diffuse[2] * diffuse_intensity * material.albedo[0],
            material.diffuse[1] * diffuse_intensity * material.albedo[0],
            material.diffuse[0] * diffuse_intensity * material.albedo[0]
        )

        # Specular component
        light_reflection = self.reflect(light_direction, intersect.normal)
        reflection_intensity = max(0, light_reflection @ direction) 
        specular_intensity =  self.light.intensity * reflection_intensity ** material.spec

        specular = (
            self.light.color[2] * specular_intensity * material.albedo[1],
            self.light.color[1] * specular_intensity * material.albedo[1],
            self.light.color[0] * specular_intensity * material.albedo[1]
        )

        result = color.color_RGB_to_GBR(
            diffuse[2] + specular[2],
            diffuse[1] + specular[1],
            diffuse[0] + specular[0]
        )

        return result