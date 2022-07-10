import matplotlib.pyplot as plt

def plot(output):
    plt.imshow(output, cmap = "gist_stern")
    plt.axis("off")
    plt.show()