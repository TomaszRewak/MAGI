from dataclasses import dataclass
from dash_extensions.enrich import Dash, Input, Output, State, Trigger, callback, ALL, MATCH
import dash_core_components as dcc
import dash_html_components as html
from dash_local_react_components import load_react_component
import random

app = Dash(__name__)

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
    WiseMan(id={'type': 'wise-man', 'name': 'melchior'}, name='melchior', order_number=1, question_id=0, answer={'id': 0, 'response': 'yes', 'status': 'yes'}),
    WiseMan(id={'type': 'wise-man', 'name': 'balthasar'}, name='balthasar', order_number=2, question_id=0, answer={'id': 0, 'response': 'yes', 'status': 'yes'}),
    WiseMan(id={'type': 'wise-man', 'name': 'casper'}, name='casper', order_number=3, question_id=0, answer={'id': 0, 'response': 'yes', 'status': 'yes'}),
    html.Div(className='title', children='MAGI'),
    html.Div(className='header', children=[
        html.Hr(),
        html.Hr(),
        html.Hr(),
        html.Hr()
    ]),
    dcc.Input(id='query', type='text', value='', debounce=True, autoComplete='off'),

    dcc.Store(id='question', data={'id': 0, 'query': ''}),
    dcc.Store(id='annotated-question', data={'id': 0, 'query': '', 'is_yes_no_question': False}),
    dcc.Store(id='is_yes_no_question', data=False),
    dcc.Store(id='question-id', data=0),
])


@callback(
    Output('question', 'data'),
    Input('query', 'value'),
    State('question', 'data'))
def question(query: str, question: dict):
    return {'id': question['id'] + 1, 'query': query}


@callback(
    Output('annotated-question', 'data'),
    Input('question', 'data'))
def annotated_question(question: dict):
    return {'id': question['id'], 'query': question['query'], 'is_yes_no_question': question['query'].endswith('?')}


@callback(
    Output('extention', 'children'),
    Input('question', 'data'),
    Input('annotated-question', 'data'))
def extention(question: dict, annotated_question: dict):
    if question['id'] != annotated_question['id']:
        return 'EXTENTION : ????'

    code = '2137' if annotated_question['is_yes_no_question'] else '3023'
    return f'EXTENTION : {code}'


@callback(
    Output({'type': 'wise-man', 'name': MATCH}, 'answer'),
    Input('annotated-question', 'data'),
    State({'type': 'wise-man', 'name': MATCH}, 'id'))
def wise_man_answer(question: dict, id: dict):
    return {'id': question['id'], 'response': 'Just an example', 'status': 'info' if not question['is_yes_no_question'] else random.choice(['yes', 'no'])}


@callback(
    Output({'type': 'wise-man', 'name': MATCH}, 'question_id'),
    Input('question', 'data'))
def question_id(question: dict):
    return question['id']


if __name__ == '__main__':
    app.run_server(debug=True)
