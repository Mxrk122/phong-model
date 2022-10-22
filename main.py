import ray
from vector3 import V3
from material import *
import color

filename = "result"
r = ray.Raytracer(filename, 800, 800)
r.change_paint_color(1, 0, 0)

brown = Material(diffuse=(153/255, 76/255, 0), albedo = [0.9, 0.1], spec = 10)
dark_brown = Material(diffuse=(125/255, 50/255, 0), albedo = [0.5, 0.5], spec = 100)
light_brown = Material(diffuse=(200/255, 157/255, 139/255), albedo = [0.5, 0.5], spec = 100)

gray = Material(diffuse=(200/255, 200/255, 200/255), albedo = [0.9, 0.1], spec = 10)
dark_blue = Material(diffuse=(0, 0, 153/255), albedo = [0.5, 0.5], spec = 100)
light_blue = Material(diffuse=(51/255, 153/255, 1), albedo = [0.5, 0.5], spec = 100)

nosexd = Material(diffuse=(1, 1, 1), albedo = [0.2, 0.8], spec = 10)

# change the light
r.set_light(V3(0, 0, -8), 10, (1, 1, 1))

#oso 1
#cuerpo
r.addSphere(V3(-5, 0, -16), 2, dark_brown)

# brazos y piernas
r.addSphere(V3(-6, 0, -14), 0.8, brown)
r.addSphere(V3(-3, 0, -14), 0.8, brown)

r.addSphere(V3(-5, 1.5, -14), 0.5, brown)
r.addSphere(V3(-4, 1.5, -14), 0.5, brown)

#cabeza
r.addSphere(V3(-4.8, -2, -15), 1.5, dark_brown)

r.addSphere(V3(-4.6, -1.4, -14.5), 1, light_brown)
r.addSphere(V3(-3.75, -1.4, -12), 0.2, nosexd)
r.addSphere(V3(-4.2, -2, -12), 0.2, nosexd)
r.addSphere(V3(-3.5, -2, -12), 0.2, nosexd)

# orejas
r.addSphere(V3(-5.5, -3, -14), 0.6, brown)
r.addSphere(V3(-3.5, -3, -14), 0.6, brown)


#oso 2
#cuerpo

r.addSphere(V3(5, 0, -16), 2, dark_blue)

# brazos y piernas
r.addSphere(V3(6, 0, -14), 0.8, gray)
r.addSphere(V3(3, 0, -14), 0.8, gray)

r.addSphere(V3(5, 1.5, -14), 0.5, gray)
r.addSphere(V3(4, 1.5, -14), 0.5, gray)

#cabeza
r.addSphere(V3(4.8, -2, -15), 1.5, gray)

r.addSphere(V3(4.6, -1.4, -14.5), 1, light_blue)
r.addSphere(V3(3.75, -1.4, -12), 0.2, nosexd)
r.addSphere(V3(4.2, -2, -12), 0.2, nosexd)
r.addSphere(V3(3.5, -2, -12), 0.2, nosexd)

# orejas
r.addSphere(V3(5.5, -3, -14), 0.6, gray)
r.addSphere(V3(3.5, -3, -14), 0.6, gray)

print("renderizando")
r.render()
r.write()