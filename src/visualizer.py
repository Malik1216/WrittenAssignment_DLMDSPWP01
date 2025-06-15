from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.io import output_file
from bokeh.palettes import Category10

def plot_training_vs_ideal(train_df, ideal_df, matches):
    output_file("training_vs_ideal.html")
    plots = []

    for train_col, ideal_col in matches.items():
        p = figure(title=f"{train_col} vs {ideal_col}", width=600, height=300)
        p.line(train_df['x'], train_df[train_col], line_width=2, color="blue", legend_label=train_col)
        p.line(ideal_df['x'], ideal_df[ideal_col], line_width=2, color="green", line_dash="dashed", legend_label=ideal_col)
        p.legend.location = "top_left"
        plots.append(p)

    show(column(*plots))

def plot_test_data_mapping(mapped_df):
    output_file("test_data_mapping.html")
    p = figure(title="Test Data Mapping to Ideal Functions", width=700, height=400)

    colors = Category10[10]
    legend_items = {}
    color_map = {}
    index = 0

    for _, row in mapped_df.iterrows():
        x = row["x"]
        y = row["y"]
        func = row["ideal_function"]

        color = "gray"
        if func:
            if func not in color_map:
                color_map[func] = colors[index % len(colors)]
                index += 1
            color = color_map[func]

        p.scatter(x, y, size=6, color=color, alpha=0.6, legend_label=str(func) if func else "Unmatched")

    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    show(p)