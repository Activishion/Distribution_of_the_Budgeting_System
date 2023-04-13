import React, { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import axios from 'axios'


const MessagePage = () => {
    const { id } = useParams()
    const [messageId, setMessageId] = useState(null)

    async function fetchMessageById(id) {
        const response = await axios.get('юрл ссылки сообщений' + id)
        setMessageId(response.data)
    }

    useEffect(() => {
        fetchMessageById(id)
    }, [])

    return( 
        <div className="messageId">
            Страница сообщения {id}
        </div>
    )
}

export default MessagePage