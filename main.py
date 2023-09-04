import os
from dash_extensions.enrich import Dash, Input, Output, State, Trigger, callback, ALL, MATCH
from dash import dcc
from dash.html import Div, Label
from dash_local_react_components import load_react_component
import ai

app = Dash(__name__)

Magi = load_react_component(app, 'components', 'magi.js')
WiseMan = load_react_component(app, 'components', 'wise_man.js')
Response = load_react_component(app, 'components', 'response.js')
Modal = load_react_component(app, 'components', 'modal.js')
Header = load_react_component(app, 'components', 'header.js')
Status = load_react_component(app, 'components', 'status.js')

app.layout = Div(
    className='system',
    children=[
        Magi(id='magi', children=[
            Header(side='left', title='質 問'),
            Header(side='right', title='解 決'),
            Status(id='status'),
            WiseMan(
                id={'type': 'wise-man', 'name': 'melchior'},
                name='melchior',
                order_number=1,
                personality='You are a scientist. Your goal is to further our understanding of the universe and advance our technological progress.'),
            WiseMan(
                id={'type': 'wise-man', 'name': 'balthasar'},
                name='balthasar',
                order_number=2,
                personality='You are a mother. Your goal is to protect your children and ensure their well-being.'),
            WiseMan(
                id={'type': 'wise-man', 'name': 'casper'},
                name='casper',
                order_number=3,
                personality='You are a woman. Your goal is to pursue love, dreams and desires.'),
            Response(id='response', status='info')
        ]),
        Div(className='input-container', children=[
            Label('access code: '),
            dcc.Input(id='key', autoComplete='off', type='password', value=os.getenv('OPENAI_API_KEY', '')),
            Label('question: '),
            dcc.Input(id='query', type='text', value='', debounce=True, autoComplete='off'),
        ]),
        Modal(id={'type': 'modal', 'name': 'melchior'}, name='melchior'),
        Modal(id={'type': 'modal', 'name': 'balthasar'}, name='balthasar'),
        Modal(id={'type': 'modal', 'name': 'casper'}, name='casper'),

        dcc.Store(id='question', data={'id': 0, 'query': ''}),
        dcc.Store(id='annotated-question', data={'id': 0, 'query': '', 'is_yes_or_no_question': False}),
        dcc.Store(id='is_yes_or_no_question', data=False),
        dcc.Store(id='question-id', data=0),
    ])


@callback(
    Output('question', 'data'),
    Input('query', 'value'),
    State('question', 'data'),
    prevent_initial_call=True)
def question(query: str, question: dict):
    return {'id': question['id'] + 1, 'query': query}


@callback(
    Output('annotated-question', 'data'),
    Input('question', 'data'),
    State('key', 'value'),
    prevent_initial_call=True)
def annotated_question(question: dict, key: str):
    try:
        is_yes_or_no_question = ai.is_yes_or_no_question(question['query'], key)

        return {
            'id': question['id'],
            'query': question['query'],
            'is_yes_or_no_question': is_yes_or_no_question,
            'error': None
        }
    except Exception as e:
        return {
            'id': question['id'],
            'query': question['query'],
            'is_yes_or_no_question': False,
            'error': str(e)
        }


@callback(
    Output('status', 'extention'),
    Input('question', 'data'),
    Input('annotated-question', 'data'))
def extention(question: dict, annotated_question: dict):
    if question['id'] != annotated_question['id']:
        return '????'

    return '7312' if annotated_question['is_yes_or_no_question'] else '3023'


@callback(
    Output({'type': 'wise-man', 'name': MATCH}, 'answer'),
    Input('annotated-question', 'data'),
    State({'type': 'wise-man', 'name': MATCH}, 'personality'),
    State('key', 'value'),
    prevent_initial_call=True)
def wise_man_answer(question: dict, personality: str, key: str):
    if question['error']:
        return {'id': question['id'], 'response': question['error'], 'status': 'error'}

    try:
        answer = ai.get_answer(question['query'], personality, key)

        if question['is_yes_or_no_question']:
            classification = ai.classify_answer(question['query'], personality, answer, key)
        else:
            classification = {'status': 'info', 'conditions': None}

        return {'id': question['id'], 'response': answer, 'status': classification['status'], 'conditions': classification['conditions'], 'error': None}

    except Exception as e:
        return {'id': question['id'], 'response': None, 'status': 'error', 'conditions': 'None', 'error': str(e)}


@callback(
    Output({'type': 'wise-man', 'name': MATCH}, 'question_id'),
    Input('question', 'data'))
def wise_man_question_id(question: dict):
    return question['id']


@callback(
    Output('response', 'question_id'),
    Input('question', 'data'))
def response_question_id(question: dict):
    return question['id']


@callback(
    Output('response', 'status'),
    Output('response', 'answer_id'),
    Input({'type': 'wise-man', 'name': ALL}, 'answer'),
    prevent_initial_call=True)
def response_status(answers: list):
    answer_id = min([answer['id'] for answer in answers])
    status = 'info'

    if any([answer['status'] == 'error' for answer in answers]):
        status = 'error'
    elif any([answer['status'] == 'no' for answer in answers]):
        status = 'no'
    elif any([answer['status'] == 'conditional' for answer in answers]):
        status = 'conditional'
    elif all([answer['status'] == 'yes' for answer in answers]):
        status = 'yes'

    return status, answer_id


@callback(
    Output({'type': 'modal', 'name': MATCH}, 'is_open'),
    Trigger({'type': 'wise-man', 'name': MATCH}, 'n_clicks'),
    prevent_initial_call=True)
def modal_visibility():
    return True


@callback(
    Output({'type': 'modal', 'name': MATCH}, 'question'),
    Output({'type': 'modal', 'name': MATCH}, 'answer'),
    Input('question', 'data'),
    Input({'type': 'wise-man', 'name': MATCH}, 'answer'))
def modal_content(question: dict, answer: dict):
    return question, answer


if __name__ == '__main__':
    app.run_server(debug=True)
