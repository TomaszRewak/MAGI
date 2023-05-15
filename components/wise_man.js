import React from 'react';


function useColor(status) {
    if (status === 'yes')
        return '#52e691';

    if (status === 'no')
        return '#a41413';

    if (status === 'info')
        return '#3caee0';

    if (status == 'conditional')
        return 'repeating-linear-gradient(56deg, rgb(82, 230, 145) 0px, rgb(82, 230, 145) 30px, #82cd68 30px, #82cd68 60px)';

    throw new Error(`Invalid status: ${status}`);
}

export default function WiseMan(props) {
    const { setProps, name, order_number, question_id, answer } = props;
    const fullName = `${name.toUpperCase()} • ${order_number}`;
    const color = useColor(answer['status']);
    const processing = question_id !== answer['id'];

    return React.createElement('div', { className: `wise-man ${name}` },
        [
            React.createElement('div', { className: `inner ${processing ? 'flicker' : ''}`, style: { background: color } }, [
                fullName
            ])
        ])
}