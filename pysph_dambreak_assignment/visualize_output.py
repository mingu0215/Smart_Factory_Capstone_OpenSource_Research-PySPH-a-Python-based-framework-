import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from pysph.solver.utils import load


def visualize_latest(output_dir, title):
    files = sorted(glob.glob(os.path.join(output_dir, "*.npz")))

    if len(files) == 0:
        print("No output files found.")
        return

    latest_file = files[-1]

    print("Loading:", latest_file)

    data = load(latest_file)

    fluid = data["arrays"]["fluid"]

    x = fluid.x
    y = fluid.y
    rho = fluid.rho

    plt.figure(figsize=(8, 6))

    scatter = plt.scatter(
        x, y,
        c=rho,
        s=10,
        cmap='jet'
    )

    plt.colorbar(scatter, label='Density')

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.axis('equal')

    plt.show()


if __name__ == "__main__":
    visualize_latest(
        "dam_break_baseline_output",
        "Baseline Dam-break"
    )
    
    
if __name__ == "__main__":
    visualize_latest(
        "dam_break_dx_modified_output",
        "DX Modified Dam-break"
    )
    
if __name__ == "__main__":
    visualize_latest(
        "dam_break_gravity_modified_output",
        "Gravity Modified Dam-break"
    )