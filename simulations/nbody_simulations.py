
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2

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
positions = np.array([[1e11, 0, 0], [-1e11, 0, 0], [0, 1e11, 0], [0, -1e11, 0]], dtype=float)
velocities = np.array([[0, 1e3, 0], [0, -1e3, 0], [-1e3, 0, 0], [1e3, 0, 0]], dtype=float)
masses = np.array([1e30, 1e30, 1e30, 1e30], dtype=float)

# Simulation parameters
dt = 1e5  # time step in seconds
num_steps = 1000  # number of simulation steps

# Arrays to store simulation data
position_history = np.zeros((num_steps, len(masses), 3))

# Run simulation
forces = calculate_forces(positions, masses)
for step in range(num_steps):
    positions, velocities, forces = update_positions(positions, velocities, forces, masses, dt)
    position_history[step] = positions

# Plot the trajectories of the particles
plt.figure(figsize=(10, 10))
for i in range(len(masses)):
    plt.plot(position_history[:, i, 0], position_history[:, i, 1], label=f'Particle {i+1}')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('N-body Simulation of Particle Trajectories')
plt.legend()
plt.grid(True)
plt.show()
