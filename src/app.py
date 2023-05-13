from dash import Dash, html                                     # pip install dash
from dash_extensions import BeforeAfter  # pip install dash-extensions==0.0.47 or higher
import dash_bootstrap_components as dbc  # dash-bootstrap-components

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H1("REHABTEC CUMPLE 10 AÑOS", style={'textAlign':'center'})
        ], width=12),
    align="center"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H2("2013-PUENTE DE LA PAZ RÍO SOGAMOSO-2023"),
            BeforeAfter(before=dict(src="/assets/juntabefore.jpg"), after=dict(src="/assets/juntaafter3.jpg"), width='100%', height='auto',value =50)
        ], width=12, style={'textAlign':'center'}),
    ],align="center"),
], fluid =True)


if __name__ == '__main__':
    app.run_server(debug=True)

    # xs = 12, sm = 12, md = 12, lg = 5, xl = 5