import matplotlib.pyplot as plt

from random_walk import RandomWalk


# New walks generate until program is active.
while True:
    # Formation of random walk and adding point to diagram.
    rw = RandomWalk(5000)
    rw.fill_walk()
    # Size of window.
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    # First and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Axis deleting.
    plt.axis(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
