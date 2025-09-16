import math
def polar_to_cartesian(r, theta):
  theta_rad = math.radians(theta)
  x = r * math.cos(theta_rad)
  y = r * math.sin(theta_rad)

  return (round(r, 5), round(y, 5))

r = float(input("Enter r:"))
theta = float(input("Enter theta:"))

print(polar_to_cartesian(r, theta))

def cartesian_to_polar(x, y):
  r = math.sqrt(x**2 + y**2)
  theta= math.degrees(math.atan2(y, x))
  return round(r, 5), round(theta, 5)

x =float(input("Enter x:"))
y = float(input("Enter y:"))

print(cartesian_to_polar(x, y))

def oscillation(A, omega, t, phi):
  phi_rad = math.radians(phi)
  x_t = A * math.cos(omega * t + phi_rad)
  return round(x_t, 5)

A = float(input("Enter amplitude A:"))
omega = float(input("Enter omega:"))
t = float(input("Enter time t:"))
phi = float(input("Enter phi (degrees):"))

print(oscillation(A, omega, t, phi))