import React from "react";

export default function Magi(props) {
    const { setProps, children } = props;

    return React.createElement("div", { className: "magi" }, children);
}