from dash import Dash, html                                     # pip install dash
from dash_extensions import BeforeAfter  # pip install dash-extensions==0.0.47 or higher
import dash_bootstrap_components as dbc  # dash-bootstrap-components
# import pathlib
#
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath('../data').resolve()


# lidfofline = [pd.read_excel(DATA_PATH.joinpath('df{}.xlsx'.format(litickers[x])), index_col=0) for x in
#               range(len(litickers))]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H1("REHABTEC CUMPLE 10 AÑOS", style={'textAlign':'center'})
        ], width=12)
    ),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H2("2013-PUENTE DE LA PAZ RÍO SOGAMOSO-2023"),
            BeforeAfter(before=dict(src="/assets/juntabefore.jpg"), after=dict(src="/assets/juntaafter2.jpg"), width='700', height='500',value =50)
        ], width=12,style={'textAlign':'center'}),
    ],className='mb-5'),
],fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True)