import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

URL = "https://raw.githubusercontent.com/IslamSaqer/Applied-Data-Science-Capstone/main/spacex_launch_dash.csv"
df = pd.read_csv(URL)
app = Dash(__name__)

sites = sorted(df["Launch Site"].dropna().unique())
app.layout = html.Div([
    html.H1("Falcon 9 Launch Analytics"),
    html.Label("Select launch site"),
    dcc.Dropdown(["All"] + sites, "All", id="site"),
    dcc.Graph(id="outcomes"),
    dcc.Graph(id="payload")
], style={"maxWidth": "1100px", "margin": "auto", "fontFamily": "Arial"})

@app.callback(
    Output("outcomes", "figure"),
    Output("payload", "figure"),
    Input("site", "value")
)
def update(site):
    d = df if site == "All" else df[df["Launch Site"] == site]
    counts = d["class"].value_counts().rename_axis("Class").reset_index(name="Launches")
    fig1 = px.bar(counts, x="Class", y="Launches", title="Landing outcome counts")
    fig2 = px.scatter(d, x="Payload Mass (kg)", y="class", color="Booster Version Category",
                      hover_data=["Flight Number"], title="Payload mass vs landing class")
    return fig1, fig2

if __name__ == "__main__":
    app.run(debug=True)
