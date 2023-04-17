import React from "react"


const RadioInputSubscription = ({ id, htmlFor, text, name }) => {
    return(
        <div className="radio">
            <input
                type="radio"
                name={name}
                id={id}
                className="radio__input"
            />
            <label
                htmlFor={htmlFor}
                className="radio__label"
            >
                {text}
            </label>
        </div>
    )
}

export default RadioInputSubscription