import React from "react";
const $ = React.createElement;

export default function Header({ side, title }) {
    const className = `header ${side}`;

    return $('div', { className },
        $('hr', {}),
        $('hr', {}),
        $('span', {}, title),
        $('hr', {}),
        $('hr', {})
    );
}