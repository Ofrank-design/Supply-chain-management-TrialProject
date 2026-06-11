"""
Supply Chain KPI Dashboard
Author: Frank Oduro — KSTU BSc Procurement & Supply Chain Management
Description: Visualises key supply chain KPIs using Python + matplotlib
             Sample data represents a typical Ghana public sector supply chain
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ─────────────────────────────────────────────
#  SAMPLE DATA  (replace with real CSV data)
# ─────────────────────────────────────────────

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 1. On-Time Delivery Rate (%)
otd = [82, 78, 85, 88, 91, 87, 83, 90, 93, 89, 94, 96]
otd_target = [90] * 12

# 2. Purchase Order Cycle Time (days)
po_cycle = [18, 21, 17, 15, 14, 16, 19, 13, 12, 14, 11, 10]
po_target = [14] * 12

# 3. Supplier Quality Rate (%)
quality = [94, 91, 93, 95, 96, 92, 90, 95, 97, 96, 98, 97]

# 4. Cost Savings vs Budget (GHS '000)
savings = [12, -5, 8, 22, 18, 15, -3, 30, 25, 20, 35, 40]

# 5. Inventory Turnover Ratio
inv_turnover = [4.2, 4.0, 4.5, 4.8, 5.1, 4.7, 4.3, 5.2, 5.5, 5.0, 5.8, 6.0]

# 6. Spend by Category (GHS '000) — Pie chart
categories    = ["Medical Supplies", "IT Equipment", "Office Supplies",
                 "Maintenance", "Logistics", "Other"]
spend_values  = [320, 210, 95, 150, 180, 75]
colors_pie    = ["#4ade80", "#60a5fa", "#f59e0b", "#f87171", "#a78bfa", "#94a3b8"]

# ─────────────────────────────────────────────
#  STYLING
# ─────────────────────────────────────────────

plt.rcParams.update({
    "figure.facecolor":  "#0a0f0d",
    "axes.facecolor":    "#111a15",
    "axes.edgecolor":    "#1e3020",
    "axes.labelcolor":   "#7a9e82",
    "axes.titlecolor":   "#e8f5ec",
    "axes.titlesize":    11,
    "axes.titleweight":  "bold",
    "axes.titlepad":     12,
    "xtick.color":       "#4a6650",
    "ytick.color":       "#4a6650",
    "xtick.labelsize":   8,
    "ytick.labelsize":   8,
    "grid.color":        "#1e3020",
    "grid.linestyle":    "--",
    "grid.alpha":        0.6,
    "text.color":        "#e8f5ec",
    "font.family":       "monospace",
    "figure.dpi":        130,
})

ACCENT   = "#4ade80"
ACCENT2  = "#86efac"
RED      = "#f87171"
YELLOW   = "#fbbf24"
BLUE     = "#60a5fa"
PURPLE   = "#a78bfa"
DIM      = "#4a6650"

# ─────────────────────────────────────────────
#  FIGURE LAYOUT  (3 rows × 2 cols)
# ─────────────────────────────────────────────

fig = plt.figure(figsize=(16, 13))
fig.suptitle(
    "Supply Chain KPI Dashboard  ·  Ghana Public Sector  ·  FY 2026",
    fontsize=15, fontweight="bold", color="#e8f5ec", y=0.97
)
fig.text(0.99, 0.97, "github.com/Ofrank-design", ha="right",
         fontsize=8, color=DIM, style="italic")

gs = fig.add_gridspec(3, 2, hspace=0.52, wspace=0.32,
                      left=0.07, right=0.97, top=0.92, bottom=0.06)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[2, 0])
ax6 = fig.add_subplot(gs[2, 1])

x = np.arange(len(months))

# ── helper: colour bars by vs-target ──────────
def bar_colors(values, target):
    return [ACCENT if v >= target[0] else RED for v in values]

# ─────────────────────────────────────────────
#  CHART 1 — On-Time Delivery Rate
# ─────────────────────────────────────────────
ax1.plot(x, otd, color=ACCENT, linewidth=2, marker="o",
         markersize=4, label="Actual", zorder=3)
ax1.plot(x, otd_target, color=YELLOW, linewidth=1.5,
         linestyle="--", label="Target (90%)", zorder=2)
ax1.fill_between(x, otd, otd_target,
                 where=[v >= t for v, t in zip(otd, otd_target)],
                 alpha=0.15, color=ACCENT)
ax1.fill_between(x, otd, otd_target,
                 where=[v < t for v, t in zip(otd, otd_target)],
                 alpha=0.15, color=RED)
ax1.set_title("On-Time Delivery Rate (%)")
ax1.set_xticks(x); ax1.set_xticklabels(months)
ax1.set_ylim(70, 100)
ax1.legend(fontsize=7, facecolor="#111a15", edgecolor="#1e3020",
           labelcolor="#7a9e82")
ax1.grid(True, axis="y")
ax1.annotate(f"Latest: {otd[-1]}%", xy=(11, otd[-1]),
             xytext=(9, otd[-1]-5), color=ACCENT2, fontsize=8,
             arrowprops=dict(arrowstyle="->", color=ACCENT2, lw=1))

# ─────────────────────────────────────────────
#  CHART 2 — PO Cycle Time
# ─────────────────────────────────────────────
bar_c = bar_colors(po_cycle, po_target)
bars = ax2.bar(x, po_cycle, color=bar_c, width=0.6, zorder=3)
ax2.plot(x, po_target, color=YELLOW, linewidth=1.5,
         linestyle="--", label="Target (14d)", zorder=4)
ax2.set_title("Purchase Order Cycle Time (days)")
ax2.set_xticks(x); ax2.set_xticklabels(months)
ax2.set_ylim(0, 26)
ax2.legend(fontsize=7, facecolor="#111a15", edgecolor="#1e3020",
           labelcolor="#7a9e82")
ax2.grid(True, axis="y")
for bar, val in zip(bars, po_cycle):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
             str(val), ha="center", va="bottom", fontsize=7,
             color="#e8f5ec")

# ─────────────────────────────────────────────
#  CHART 3 — Supplier Quality Rate
# ─────────────────────────────────────────────
ax3.plot(x, quality, color=BLUE, linewidth=2, marker="s",
         markersize=4, label="Quality Rate")
ax3.fill_between(x, quality, 88, alpha=0.12, color=BLUE)
ax3.axhline(95, color=YELLOW, linestyle="--", linewidth=1.5,
            label="Target (95%)")
ax3.set_title("Supplier Quality Rate (%)")
ax3.set_xticks(x); ax3.set_xticklabels(months)
ax3.set_ylim(85, 100)
ax3.legend(fontsize=7, facecolor="#111a15", edgecolor="#1e3020",
           labelcolor="#7a9e82")
ax3.grid(True, axis="y")

# ─────────────────────────────────────────────
#  CHART 4 — Cost Savings vs Budget
# ─────────────────────────────────────────────
colors_savings = [ACCENT if v >= 0 else RED for v in savings]
bars4 = ax4.bar(x, savings, color=colors_savings, width=0.6, zorder=3)
ax4.axhline(0, color=DIM, linewidth=1)
ax4.set_title("Cost Savings vs Budget (GHS '000)")
ax4.set_xticks(x); ax4.set_xticklabels(months)
ax4.grid(True, axis="y")
total_savings = sum(savings)
ax4.text(0.98, 0.95, f"YTD: GHS {total_savings}k",
         transform=ax4.transAxes, ha="right", va="top",
         fontsize=9, color=ACCENT if total_savings >= 0 else RED,
         fontweight="bold")

# ─────────────────────────────────────────────
#  CHART 5 — Inventory Turnover
# ─────────────────────────────────────────────
ax5.plot(x, inv_turnover, color=PURPLE, linewidth=2,
         marker="D", markersize=4, label="Turnover Ratio")
ax5.fill_between(x, inv_turnover, 4.0, alpha=0.12, color=PURPLE)
ax5.axhline(5.0, color=YELLOW, linestyle="--", linewidth=1.5,
            label="Target (5.0)")
ax5.set_title("Inventory Turnover Ratio")
ax5.set_xticks(x); ax5.set_xticklabels(months)
ax5.set_ylim(3.5, 6.5)
ax5.legend(fontsize=7, facecolor="#111a15", edgecolor="#1e3020",
           labelcolor="#7a9e82")
ax5.grid(True, axis="y")

# ─────────────────────────────────────────────
#  CHART 6 — Spend by Category (Pie)
# ─────────────────────────────────────────────
wedges, texts, autotexts = ax6.pie(
    spend_values,
    labels=categories,
    colors=colors_pie,
    autopct="%1.1f%%",
    startangle=140,
    pctdistance=0.78,
    wedgeprops=dict(linewidth=1.5, edgecolor="#0a0f0d")
)
for t in texts:
    t.set_fontsize(8); t.set_color("#7a9e82")
for at in autotexts:
    at.set_fontsize(7); at.set_color("#0a0f0d"); at.set_fontweight("bold")
ax6.set_title("Annual Spend by Category (GHS '000)")
total_spend = sum(spend_values)
ax6.text(0, -1.45, f"Total Spend: GHS {total_spend}k",
         ha="center", fontsize=9, color=ACCENT2, fontweight="bold")

# ─────────────────────────────────────────────
#  SCORECARD ROW  (text annotations at bottom)
# ─────────────────────────────────────────────
scorecard = [
    ("OTD Rate",     f"{otd[-1]}%",        otd[-1] >= 90),
    ("PO Cycle",     f"{po_cycle[-1]}d",   po_cycle[-1] <= 14),
    ("Quality",      f"{quality[-1]}%",    quality[-1] >= 95),
    ("YTD Savings",  f"GHS {total_savings}k", total_savings >= 0),
    ("Inv. Turnover",f"{inv_turnover[-1]}x", inv_turnover[-1] >= 5.0),
]

fig.text(0.5, 0.015, "KPI SCORECARD (Dec)",
         ha="center", fontsize=9, color=DIM, fontweight="bold")
for i, (label, value, ok) in enumerate(scorecard):
    xpos = 0.1 + i * 0.18
    color = ACCENT if ok else RED
    status = "▲ ON TARGET" if ok else "▼ BELOW"
    fig.text(xpos, 0.033, label,   ha="center", fontsize=7,  color=DIM)
    fig.text(xpos, 0.022, value,   ha="center", fontsize=10, color=color, fontweight="bold")
    fig.text(xpos, 0.010, status,  ha="center", fontsize=6,  color=color)

plt.savefig("scm_kpi_dashboard.png", dpi=130,
            bbox_inches="tight", facecolor="#0a0f0d")
print("✅ Dashboard saved as scm_kpi_dashboard.png")
plt.show()
