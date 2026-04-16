import numpy as np
import matplotlib.pyplot as plt
from pyscript import display
from js import document

def make_graph():
    # Generate values
    numbers = np.arange(1, 6)
    doubled = numbers * 3   # different from original (x3 instead of x2)

    # Show text output
    output_text = "Numbers: " + str(numbers) + " | Result: " + str(doubled)
    document.getElementById("result").innerText = output_text

    # Create a new figure
    plt.clf()
    plt.plot(numbers, doubled)
    plt.title("Sample Output")

    # Show graph inside page
    display(plt.gcf(), target="result")
