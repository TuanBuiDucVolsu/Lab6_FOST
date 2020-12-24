from vpython import *
from scene import *
scale = 1e-10

scene.range = 0.3*scale

R = scale
qe = 1.6e-19
KE = 1e5*1.6e-19 # eV*conversion_factor_to_J
kel = 9e9
range_of_particles = arange(scale*0.04,scale*0.08,scale*0.005)

alphas = []

for i in range_of_particles:
    particle = sphere(radius=0.001*R,make_trail=True,stop=False)
    particle.mass = 4*1.67e-27 # kg
    particle.charge = 2*qe
    particle.pos = vec(-0.6*scale, i, 0)
    particle.mom = sqrt(2*particle.mass*KE)*vec(1,0,0)
    alphas.append(particle)

gold = sphere(color=color.yellow,radius=0.03*scale)
gold.charge = 79*qe


dt = 1e-18

while True:
    rate(20)
    for particle in alphas:
        if particle.stop == False:
            runit = particle.pos/mag(particle.pos)
            F = kel*particle.charge*gold.charge/mag2(particle.pos)*runit
            particle.mom = particle.mom + F*dt
            particle.pos = particle.pos + (particle.mom/particle.mass)*dt
            #print(particle.mom)
        #if mag(particle.pos) < 1:
        #    particle.stop = True
        if mag(particle.pos) > 2*scale:
            particle.stop = True
