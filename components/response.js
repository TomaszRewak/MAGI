import React from 'react';

function getStatusText(status) {
    if (status === 'info')
        return '情 報';

    if (status === 'yes')
        return '合 意';

    if (status === 'no')
        return '拒 絶';

    if (status === 'conditional')
        return '状 態';

    if (status === 'error')
        return '誤 差'

    throw new Error('Invalid status: ' + status);
}

function getStatusColor(status) {
    if (status === 'info')
        return '#3caee0';

    if (status === 'yes')
        return '#52e691';

    if (status === 'no')
        return '#a41413';

    if (status === 'conditional')
        return '#ff8d00';

    if (status === 'error')
        return 'gray';

    throw new Error('Invalid status: ' + status);
}

export default function Response(props) {
    const { status } = props;

    const text = getStatusText(status);
    const color = getStatusColor(status);

    return React.createElement('div', { className: 'response', style: { color: color, borderColor: color } },
        [
            React.createElement('div', { className: 'inner' }, [text])
        ]);
}