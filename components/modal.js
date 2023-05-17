import React from 'react';
const $ = React.createElement;

export default function Modal({ setProps, name, is_open, question, answer }) {
    if (!is_open) return null;

    const questionId = question.id;
    const answerId = answer.id;

    if (questionId !== answerId)
        answer = { id: questionId, status: 'error', error: 'loading...' };

    const close = () => {
        setProps({ is_open: false });
    };

    return $('div', { className: 'modal' },
        $('div', { className: 'modal-header' },
            $('div', { className: 'modal-title' }, name),
            $('div', { className: 'close', onClick: close }, 'X'),
        ),
        $('div', { className: 'modal-body' },
            $('div', {}, 'question: '),
            $('div', {}, question.query),
            $('div', {}, 'status: '),
            $('div', {}, answer.status),
            $('div', {}, 'error: '),
            $('div', {}, answer.error),
            $('div', {}, 'conditions: '),
            $('div', {}, answer.conditions),
            $('div', {}, 'full response: '),
            $('div', {}, answer.response)
        ),
    );
}