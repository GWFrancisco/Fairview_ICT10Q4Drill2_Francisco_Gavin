import numpy as np
import matplotlib.pyplot as plt
from pyscript import display
from js import document

def run_demo():

    # Create data
    x = np.arange(0, 6)
    y = x + 5

    # Show text output in HTML
    document.getElementById("output").innerText = (
        f"X values: {x} | Y values: {y}"
    )

    # Clear old plot
    plt.clf()

    # Plot graph
    plt.plot(x, y)
    plt.title("Simple Linear Graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    # Display in browser
    display(plt.gcf(), target="output")