import React from 'react';


function useColor(status) {
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

export default function WiseMan(props) {
    const { setProps, name, order_number, question_id, answer, n_clicks } = props;
    const fullName = `${name.toUpperCase()} • ${order_number}`;
    const color = useColor(answer['status']);
    const processing = question_id !== answer['id'];

    const onClick = () => {
        setProps({ n_clicks: n_clicks + 1 });
    };

    return React.createElement('div', { className: `wise-man ${name}`, onClick: onClick, key: name },
        [
            React.createElement('div', { className: `inner ${processing ? 'flicker' : ''}`, style: { background: color } }, [
                fullName
            ])
        ])
}

WiseMan.defaultProps = {
    n_clicks: 0
};