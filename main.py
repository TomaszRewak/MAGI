from dash import Dash, Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash_local_react_components import load_react_component

app = Dash(__name__)

Magi = load_react_component(app, 'components', 'magi.js')
WiseMan = load_react_component(app, 'components', 'wise_man.js')

app.layout = Magi(id='magi', children=[
    WiseMan(id='melchior', name='MELCHIOR', order_number=1, status='yes'),
    WiseMan(id='baltasar', name='BALTASAR', order_number=2, status='no'),
    WiseMan(id='casper', name='CASPAR', order_number=3, status='info'),
    dcc.Input(id='query', type='text'),
    html.Button(id='send-button', children='Send')
])

if __name__ == '__main__':
    app.run_server(debug=True)
