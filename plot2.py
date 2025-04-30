import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(32, 5), facecolor='none')  # Wider for horizontal
ax.set_xlim(0, 32)
ax.set_ylim(0, 10)
ax.axis('off')

# Define blocks: (x-position, width, label)
blocks = [
    (0, 6, 'Disk Storage (Optional)'),
    (6.5, 6, 'Host RAM: Buffer Storage'),
    (13, 6, 'Host RAM: Offloaded Layers'),
    (19.5, 6, 'GPU VRAM: Critical Operations'),
    (26, 6, 'GPU VRAM: Active Layers'),
]
colors = ['#FFA500', '#A9A9A9', '#D3D3D3', '#4682B4', '#87CEFA']

# Draw blocks
for (x, w, label), color in zip(blocks, colors):
    rect = Rectangle((x, 2), w, 6, facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    formatted_label = label.replace(': ', ':\n')
    ax.text(x + w/2, 5, formatted_label, va='center', ha='center', fontsize=30, fontweight='bold')

# Draw arrows between blocks
for i in range(len(blocks)-1):
    x_start = blocks[i][0] + blocks[i][1]  # end of current block
    x_end = blocks[i+1][0]  # start of next block
    arrow = FancyArrowPatch((x_start, 5), (x_end, 5), arrowstyle='-|>', mutation_scale=18, linewidth=1.5)
    ax.add_patch(arrow)

fig.suptitle("Dynamic Offloading Architecture (Horizontal View)", fontsize=20, fontweight='bold')
plt.tight_layout()
plt.savefig("dynamic_offloading_architecture.png", transparent=True)
plt.show()
