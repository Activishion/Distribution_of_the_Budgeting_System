import React from "react"


const ButtonForm = ({ form }) => {
    return(
        <div className="container_button">
            <button
                type="submit"
                form={form}
            >
                Отправить
            </button>
        </div>
    )
}

export default ButtonForm