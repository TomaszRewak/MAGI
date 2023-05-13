from dataclasses import dataclass
from dash_extensions.enrich import Dash, Input, Output, callback
import dash_core_components as dcc
import dash_html_components as html
from dash_local_react_components import load_react_component

app = Dash(__name__)


@dataclass
class WiseManDefinition:
    id: str
    name: str
    order_number: int
    system_prompt: str


wise_man = [
    WiseManDefinition(id='melchior', name='MELCHIOR', order_number=1, system_prompt='You are a wise man'),
    WiseManDefinition(id='baltasar', name='BALTASAR', order_number=2, system_prompt='You are a wise man'),
    WiseManDefinition(id='casper', name='CASPAR', order_number=3, system_prompt='You are a wise man'),
]

Magi = load_react_component(app, 'components', 'magi.js')
WiseMan = load_react_component(app, 'components', 'wise_man.js')

# 質問 - question
# 解決 - resolution

app.layout = Magi(id='magi', children=[
    WiseMan(id='melchior', name='MELCHIOR', order_number=1, status='yes'),
    WiseMan(id='baltasar', name='BALTASAR', order_number=2, status='no'),
    WiseMan(id='casper', name='CASPAR', order_number=3, status='info'),
    dcc.Input(id='query', type='text'),
    html.Button(id='send-button', children='Send')
])

if __name__ == '__main__':
    app.run_server(debug=True)
