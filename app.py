from shiny.express import input, render, ui
from shinywidgets import render_plotly 

ui.page_opts(title="Paris Olympic 2024 Visualizations", fillable=True)

with ui.sidebar():
    ui.input_selectize(
        "var", "Select variable",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "year"]
    )
    ui.input_numeric("bins", "Number of bins", 30)

with ui.card(full_screen=True):
    @render_plotly
    def hist():
        import plotly.express as px
        from palmerpenguins import load_penguins
        return px.histogram(load_penguins(), x=input.var(), nbins=input.bins())