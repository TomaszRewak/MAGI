import React from 'react';

export default function Modal({ setProps, name, is_open, question, answer }) {
    if (!is_open) return null;

    const questionId = question.id;
    const answerId = answer.id;

    if (questionId !== answerId)
        answer = { id: questionId, status: 'error', error: 'questionId !== answerId' };

    const close = () => {
        setProps({ is_open: false });
    };

    return React.createElement('div', { className: 'modal' }, [
        React.createElement('div', { className: 'modal-header' }, [
            React.createElement('div', { className: 'modal-title' }, [name]),
            React.createElement('div', { className: 'close', onClick: close }, ['X']),
        ]),
        React.createElement('div', { className: 'modal-body' }, [
            React.createElement('div', {}, 'question: '),
            React.createElement('div', {}, question.query),
            React.createElement('div', {}, 'status: '),
            React.createElement('div', {}, answer.status),
            React.createElement('div', {}, 'error: '),
            React.createElement('div', {}, answer.error),
            React.createElement('div', {}, 'conditions: '),
            React.createElement('div', {}, answer.conditions),
            React.createElement('div', {}, 'full response: '),
            React.createElement('div', {}, answer.response)
        ]),
    ]);
}