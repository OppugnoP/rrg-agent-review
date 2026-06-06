import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from pathlib import Path

OUT_DIR = Path(__file__).parent / "results"
OUT_DIR.mkdir(exist_ok=True)

plt.rcParams['font.family'] = 'Times New Roman'

# =========================
# 预测2026年总文章数
# =========================
x_hist = np.array([2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
y_hist = np.array([1, 2, 3, 8, 8, 19, 34, 51, 83, 132])

x_shifted = x_hist - 2016
a, b = np.polyfit(x_shifted, np.log(y_hist), 1)
total_2026 = int(np.exp(a * (2026 - 2016) + b))

print(f"Predicted total articles in 2026: {total_2026}")

# =========================
# 数据
# =========================
years = [2023, 2024, 2025, 2026]
articles_total = [51, 83, 132, total_2026]
ratios         = [10.42, 21.95, 49.22, 68.00]
llm_2026       = round(total_2026 * ratios[3] / 100)
articles_llm   = [5, 18, 63, llm_2026]


# =========================
# 通用绘图函数
# =========================
def plot_curve(ax, x, y, use_dashed=True):
    ax.plot(x[:3], y[:3],
            color='#1f77b4', linewidth=2.2, linestyle='-', marker='o', markersize=5)
    ax.plot(x[2:], y[2:],
            color='#1f77b4', linewidth=2.2,
            linestyle='--' if use_dashed else '-', marker='o', markersize=5)

    ax.grid(True, linestyle='--', linewidth=0.6, color='gray', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['bottom'].set_linewidth(1.0)
    ax.tick_params(axis='both', direction='in', length=4, width=1,
                   colors='black', labelsize=15)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlim(2022.5, 2026.5)
    ax.set_xlabel("Year", fontsize=15)


# =========================
# 图1：Total Number of Articles
# =========================
fig1, ax1 = plt.subplots(figsize=(4.2, 3.8), dpi=300)
plot_curve(ax1, years, articles_total)
ax1.set_ylim(0, 300)
plt.tight_layout()
plt.savefig(OUT_DIR / "total_number.pdf", bbox_inches='tight')

# =========================
# 图2：LLM-based Number of Articles
# =========================
fig2, ax2 = plt.subplots(figsize=(4.2, 3.8), dpi=300)
plot_curve(ax2, years, articles_llm)
ax2.set_ylim(0, 200)
plt.tight_layout()
plt.savefig(OUT_DIR / "llm_number.pdf", bbox_inches='tight')

# =========================
# 图3：LLM-based Ratio
# =========================
fig3, ax3 = plt.subplots(figsize=(4.2, 3.8), dpi=300)
plot_curve(ax3, years, ratios, use_dashed=False)
ax3.set_ylim(0, 80)
ax3.set_yticks([0, 20, 40, 60, 80])
ax3.set_yticklabels(['0%', '20%', '40%', '60%', '80%'])
plt.tight_layout()
plt.savefig(OUT_DIR / "llm_ratio.pdf", bbox_inches='tight')

plt.show()
