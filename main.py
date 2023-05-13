from dataclasses import dataclass
from dash_extensions.enrich import Dash, Input, Output, State, Trigger, callback, ALL, MATCH
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
    WiseManDefinition(id='melchior', name='MELCHIOR',
                      order_number=1, system_prompt='You are a wise man'),
    WiseManDefinition(id='baltasar', name='BALTASAR',
                      order_number=2, system_prompt='You are a wise man'),
    WiseManDefinition(id='casper', name='CASPAR', order_number=3,
                      system_prompt='You are a wise man'),
]

Magi = load_react_component(app, 'components', 'magi.js')
WiseMan = load_react_component(app, 'components', 'wise_man.js')

# 質問 - question
# 解決 - resolution

app.layout = Magi(id='magi', children=[
    html.Div(
        className='system-status',
        children=[
            html.Div(children='CODE : 473'),
            html.Div(children='FILE : MAGI_SYS'),
            html.Div(id='extention', children='EXTENTION : ????'),
            html.Div(children='EX_MODE : OFF'),
            html.Div(children='PRIORITY : AAA')]),
    WiseMan(id={'type': 'wise-man', 'name': 'melchior'},
            name='MELCHIOR', order_number=1, status='yes'),
    WiseMan(id={'type': 'wise-man', 'name': 'baltasar'},
            name='BALTASAR', order_number=2, status='no'),
    WiseMan(id={'type': 'wise-man', 'name': 'casper'},
            name='CASPAR', order_number=3, status='info'),
    dcc.Input(id='query', type='text', value='',
              debounce=True, autoComplete='off'),
    dcc.Store(id='is_yes_no_question', data=False)
])


@callback(
    Output('is_yes_no_question', 'data'),
    Input('query', 'value'),
    prevent_initial_call=True)
def is_yes_no_question(query: str):
    print('Checking if question is a yes/no question')
    return query.endswith('?')


@callback(
    Output('extention', 'children'),
    Input('is_yes_no_question', 'data'))
def extention(is_yes_no_question: bool):
    code = '2137' if is_yes_no_question else '3023'
    return f'EXTENTION : {code}'


@callback(
    Output({'type': 'wise-man', 'name': MATCH}, 'status'),
    Input('is_yes_no_question', 'data'))
def wise_man_status(is_yes_no_question: bool):
    return 'yes' if is_yes_no_question else 'info'


if __name__ == '__main__':
    app.run_server(debug=True)
