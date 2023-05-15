from dataclasses import dataclass
import os
from dash_extensions.enrich import Dash, Input, Output, State, Trigger, callback, ALL, MATCH
import dash_core_components as dcc
import dash_html_components as html
from dash_local_react_components import load_react_component
import random
import ai

app = Dash(__name__)

Magi = load_react_component(app, 'components', 'magi.js')
WiseMan = load_react_component(app, 'components', 'wise_man.js')
Response = load_react_component(app, 'components', 'response.js')

app.layout = html.Div(children=[
    Magi(id='magi', children=[
        html.Div(className='connection casper-balthasar'),
        html.Div(className='connection casper-melchior'),
        html.Div(className='connection balthasar-melchior'),
        html.Div(
            className='system-status',
            children=[
                html.Div(children='CODE:473'),
                html.Div(children='FILE:MAGI_SYS'),
                html.Div(id='extention', children='EXTENTION:????'),
                html.Div(children='EX_MODE:OFF'),
                html.Div(children='PRIORITY:AAA')]),
        WiseMan(
            id={'type': 'wise-man', 'name': 'melchior'},
            name='melchior',
            order_number=1,
            personality='You are a scientist. Your goal is to further our our understanding of the universe and advance our technological progress.',
            question_id=0,
            answer={'id': 0, 'response': 'yes', 'status': 'yes'}),
        WiseMan(
            id={'type': 'wise-man', 'name': 'balthasar'},
            name='balthasar',
            order_number=2,
            personality='You are a mother. Your goal is to protect your children and ensure their well-being.',
            question_id=0,
            answer={'id': 0, 'response': 'yes', 'status': 'yes'}),
        WiseMan(
            id={'type': 'wise-man', 'name': 'casper'},
            name='casper',
            order_number=3,
            personality='You are a woman. Your goal is to pursue your dreams and desires.',
            question_id=0,
            answer={'id': 0, 'response': 'yes', 'status': 'yes'}),
        Response(id='response', status='info'),
        html.Div(className='title', children='MAGI'),
        html.Div(className='header left', children=[
            html.Hr(),
            html.Hr(),
            html.Span('質 問 '),
            html.Hr(),
            html.Hr()
        ]),
        html.Div(className='header right', children=[
            html.Hr(),
            html.Hr(),
            html.Span('解 決 '),
            html.Hr(),
            html.Hr()
        ])
    ]),
    html.Label('MAGI access codes: '),
    dcc.Input(id='key', autoComplete='off', type='password', value=os.getenv('OPENAI_API_KEY', '')),
    dcc.Input(id='query', type='text', value='', debounce=True, autoComplete='off'),

    dcc.Store(id='question', data={'id': 0, 'query': ''}),
    dcc.Store(id='annotated-question', data={'id': 0, 'query': '', 'is_yes_no_question': False}),
    dcc.Store(id='is_yes_no_question', data=False),
    dcc.Store(id='question-id', data=0),
])


@callback(
    Output('question', 'data'),
    Input('query', 'value'),
    State('question', 'data'),
    prevent_initial_call=True)
def question(query: str, question: dict):
    print('question')

    return {'id': question['id'] + 1, 'query': query}


@callback(
    Output('annotated-question', 'data'),
    Input('question', 'data'),
    State('key', 'value'),
    prevent_initial_call=True)
def annotated_question(question: dict, key: str):
    print('annotated_question')

    is_yes_no_question = ai.is_yes_or_no_question(question['query'], key)

    return {'id': question['id'], 'query': question['query'], 'is_yes_no_question': is_yes_no_question}


@callback(
    Output('extention', 'children'),
    Input('question', 'data'),
    Input('annotated-question', 'data'))
def extention(question: dict, annotated_question: dict):
    if question['id'] != annotated_question['id']:
        return 'EXTENTION:????'

    code = '2137' if annotated_question['is_yes_no_question'] else '3023'
    return f'EXTENTION:{code}'


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


@callback(
    Output('response', 'status'),
    Input({'type': 'wise-man', 'name': ALL}, 'answer'))
def response_status(answers: list):
    if all([answer['status'] == 'yes' for answer in answers]):
        return 'yes'
    elif any([answer['status'] == 'no' for answer in answers]):
        return 'no'
    else:
        return 'info'


if __name__ == '__main__':
    app.run_server(debug=True)
