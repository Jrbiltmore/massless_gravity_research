
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
H0 = 70 * 1e3 / (3.086e22)  # Hubble constant in s^-1 (70 km/s/Mpc converted to m/s/Mpc and then to s^-1)

# Function to calculate the density of the universe
def calculate_density(a, Omega_m0, Omega_lambda0):
    rho_critical = 3 * (H0**2) / (8 * np.pi * G)
    rho_m = Omega_m0 * rho_critical / a**3
    rho_lambda = Omega_lambda0 * rho_critical
    return rho_m + rho_lambda

# Function to calculate gravitational forces
def calculate_forces(positions, masses):
    num_particles = len(masses)
    forces = np.zeros((num_particles, 3))
    for i in range(num_particles):
        for j in range(num_particles):
            if i != j:
                r = positions[j] - positions[i]
                distance = np.linalg.norm(r)
                force_magnitude = G * masses[i] * masses[j] / distance**2
                forces[i] += force_magnitude * r / distance
    return forces

# Function to update positions and velocities
def update_positions(positions, velocities, forces, masses, dt):
    new_positions = positions + velocities * dt + 0.5 * forces / masses[:, np.newaxis] * dt**2
    new_forces = calculate_forces(new_positions, masses)
    new_velocities = velocities + 0.5 * (forces + new_forces) / masses[:, np.newaxis] * dt
    return new_positions, new_velocities, new_forces

# Initialize positions, velocities, and masses
num_particles = 100  # Number of particles
positions = np.random.rand(num_particles, 3) * 1e23  # Random initial positions in meters
velocities = np.random.rand(num_particles, 3) * 1e3  # Random initial velocities in m/s
masses = np.ones(num_particles) * 1e30  # Uniform mass for all particles in kg

# Simulation parameters
dt = 1e14  # time step in seconds
num_steps = 1000  # number of simulation steps

# Arrays to store simulation data
position_history = np.zeros((num_steps, num_particles, 3))

# Run simulation
forces = calculate_forces(positions, masses)
for step in range(num_steps):
    positions, velocities, forces = update_positions(positions, velocities, forces, masses, dt)
    position_history[step] = positions

# Plot the trajectories of a few particles
plt.figure(figsize=(10, 10))
for i in range(5):  # Plot trajectories of the first 5 particles
    plt.plot(position_history[:, i, 0], position_history[:, i, 1], label=f'Particle {i+1}')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Cosmological Simulation of Particle Trajectories')
plt.legend()
plt.grid(True)
plt.show()
