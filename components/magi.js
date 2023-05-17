import React from "react";
const $ = React.createElement;

export default function Magi({ children }) {
    return $('div', { className: 'magi' },
        $('div', { className: 'connection casper-balthasar' }),
        $('div', { className: 'connection casper-melchior' }),
        $('div', { className: 'connection balthasar-melchior' }),
        ...children,
        $('div', { className: 'title' }, 'MAGI')
    );
}