import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

def plot_yearly_distribution():
    # Expanded year-wise data
    years = [str(year) for year in range(1960, 2026)]
    window_size = 5
    start = 0

    # Sample data for age groups and gender distribution
    age_groups = ['0-18', '19-35', '36-60', '60+']
    genders = ['Male', 'Female']

    # Generate sample population data: shape (years, age_groups, genders)
    np.random.seed(0)
    data = np.random.randint(50, 150, size=(len(years), len(age_groups), len(genders)))

    # Colors for each age group and gender combination
    colors = {
        ('0-18', 'Male'): 'dodgerblue',
        ('0-18', 'Female'): 'deepskyblue',
        ('19-35', 'Male'): 'mediumseagreen',
        ('19-35', 'Female'): 'lightgreen',
        ('36-60', 'Male'): 'gold',
        ('36-60', 'Female'): 'khaki',
        ('60+', 'Male'): 'coral',
        ('60+', 'Female'): 'lightcoral'
    }

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    def plot_bars(pos):
        ax.clear()
        bottom = np.zeros(window_size)
        for age in age_groups:
            for gender in genders:
                values = data[pos:pos+window_size, age_groups.index(age), genders.index(gender)]
                ax.bar(years[pos:pos+window_size], values, bottom=bottom,
                       color=colors[(age, gender)], label=f'{age} {gender}')
                bottom += values
        ax.set_title('Yearly Population Growth with Age and Gender Distribution')
        ax.set_xlabel('Year')
        ax.set_ylabel('Population Count')
        ax.grid(axis='y', linestyle='--', alpha=0.6)
        # Remove duplicate labels in legend
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.05, 1), loc='upper left')
        # Add value labels on top of bars with percentage
        for rects in ax.containers:
            total_height = sum([rect.get_height() for rect in rects])
            for rect in rects:
                height = rect.get_height()
                if height > 0:
                    percent = (height / total_height) * 100 if total_height > 0 else 0
                    ax.text(rect.get_x() + rect.get_width() / 2, rect.get_y() + height / 2,
                            f'{int(height)}\n({percent:.1f}%)', ha='center', va='center', fontsize=7, color='black')

    plot_bars(start)

    ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
    slider = Slider(ax_slider, 'Year Range', 0, len(years) - window_size, valinit=start, valstep=1)

    def update(val):
        pos = int(slider.val)
        plot_bars(pos)
        fig.canvas.draw_idle()

    slider.on_changed(update)

    plt.show()

if __name__ == "__main__":
    plot_yearly_distribution()
