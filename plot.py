import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

# ========================
# High-level architecture
# ========================
fig, ax = plt.subplots(figsize=(5, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 36)
ax.axis('off')

blocks = [
    (32, 4, 'Embedding', '#FFA500'),       # Orange
    (12, 20, 'Decoder Layers (×32)', '#ADD8E6'),  # Light Blue
    (6, 4, 'Final Norm', '#D3D3D3'),        # Light Gray
    (1, 4, 'LM Head', '#FF6F61'),           # Soft Red
]

for y, h, label, color in blocks:
    rect = Rectangle((1, y), 8, h, facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    formatted_label = label.replace(' ', '\n')
    ax.text(
        5, y + h/2, formatted_label, 
        va='center', ha='center',
        fontsize=30, fontweight='bold'
    )

arrows = [
    ((5, 32), (5, 31)),
    ((5, 12), (5, 10)),
    ((5, 6), (5, 5)),
]
for start, end in arrows:
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle='-|>', mutation_scale=18,
        linewidth=1.5, color='black'
    )
    ax.add_patch(arrow)

plt.tight_layout()
plt.savefig("high_level_architecture.png", dpi=300, transparent=True)
plt.show()

# =========================
# Decoder Layer Detail
# =========================
fig2, ax2 = plt.subplots(figsize=(5, 12))
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 36)
ax2.axis('off')

components = [
    (14, 'Self-Attention', '#87CEFA'),   # LightSkyBlue
    (11.5, 'LayerNorm', '#D3D3D3'),      # Light Gray
    (9, 'GateProj', '#BA55D3'),          # MediumOrchid
    (6.5, 'UpProj', '#BA55D3'),          # Same
    (4, 'DownProj', '#BA55D3'),          # Same
    (1.5, 'LayerNorm', '#D3D3D3'),       # Light Gray
]
width, height = 2, 2

for y, label, color in components:
    rect = Rectangle(
        (0.5, y), width, height, 
        facecolor=color, 
        edgecolor='black', 
        linewidth=1.5
    )
    ax2.add_patch(rect)
    formatted_label = label.replace('-', '-\n')
    ax2.text(
        0.5 + width/2, 
        y + height/2, 
        formatted_label,         
        va='center', ha='center',
        fontsize=30, fontweight='bold'
    )

for i in range(len(components) - 1):
    start = (0.5 + width / 2, components[i][0])
    end = (0.5 + width / 2, components[i + 1][0] + height)
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle='-|>', mutation_scale=18,
        linewidth=1.5, color='black'
    )
    ax2.add_patch(arrow)

fig2.suptitle(
    'Decoder Layer Detailed Structure (Vertical)', 
    fontsize=16, fontweight='bold', y=1.03
)

plt.tight_layout()
plt.savefig("decoder_layer_detail.png", dpi=300, transparent=True)
plt.show()
