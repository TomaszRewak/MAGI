import React from 'react';
const $ = React.createElement;

export default function Status({ extention }) {
    const extentionLabel = `EXTENTION:${extention}`;

    return $('div', { className: 'system-status' },
        $('div', {}, 'CODE:473'),
        $('div', {}, 'FILE:MAGI_SYS'),
        $('div', {}, extentionLabel),
        $('div', {}, 'EX_MODE:OFF'),
        $('div', {}, 'PRIORITY:AAA')
    );
}

Status.defaultProps = {
    extention: '????'
};