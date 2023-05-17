import React from 'react';
const $ = React.createElement;

function getColor(status) {
    if (status === 'yes')
        return '#52e691';

    if (status === 'no')
        return '#a41413';

    if (status === 'info')
        return '#3caee0';

    if (status === 'conditional')
        return 'repeating-linear-gradient(56deg, rgb(82, 230, 145) 0px, rgb(82, 230, 145) 30px, #82cd68 30px, #82cd68 60px)';

    if (status === 'error')
        return 'black';

    throw new Error(`Invalid status: ${status}`);
}

export default function WiseMan({ setProps, name, order_number, question_id, answer, n_clicks }) {
    const fullName = `${name.toUpperCase()} • ${order_number}`;
    const color = getColor(answer['status']);
    const processing = question_id !== answer['id'];

    const onClick = () => {
        setProps({ n_clicks: n_clicks + 1 });
    };

    let outerClassName = `wise-man ${name}`;
    let innerClassName = 'inner';
    if (processing)
        innerClassName += ' flicker';

    return $('div', { className: outerClassName, onClick: onClick, key: name },
        $('div', { className: innerClassName, style: { background: color } }, fullName)
    )
}

WiseMan.defaultProps = {
    n_clicks: 0,
    question_id: 0,
    answer: {
        id: 0,
        status: 'info',
        error: '',
        conditions: '',
        response: 'Waiting for query...'
    }
};