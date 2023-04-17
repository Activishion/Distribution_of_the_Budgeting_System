import React, { useEffect, useState } from "react"
import { useNavigate, useParams } from "react-router-dom"
import axios from 'axios'

import MessageText from '../UI/Container/MessageText'


const MessagePage = () => {
    const nav = useNavigate()
    const { id } = useParams()
    const [messageId, setMessageId] = useState(null)

    async function GetMessageById(id) {
        const response = await axios.get('юрл ссылки сообщений' + id)
        setMessageId(response.data)
    }

    useEffect(() => {
        GetMessageById(id)
    }, [])

    return (
        <div className="messageId">
            <div className="message_header">
                <p className="message_header_text">Сообщение - {id}</p>
                <div className="paodzo_flex">
                    <MessageText
                        header='Отправлено: '
                        text='17:37:23 14.04.2023'
                    />
                </div>
            </div>
            <div className="paodzo">
                <div className="paodzo_flex">
                    <MessageText
                        header='ПАО: '
                        text='Да'
                    />
                </div>
                <div className="paodzo_flex">
                    <MessageText
                        header='ДЗО: '
                        text='Да'
                    />
                </div>
            </div>
            <div className="main">
                <p className="main_h">Тема сообщения</p>
                <p className="main_text">
                    Текст сообщения
                </p>
            </div>
            <div className="author">
                <MessageText
                    header='Автор: '
                    text='Маравье Степан Валерьевич'
                />
            </div>
            <div className="bottom_container">
                <button
                    className="message_button"
                    onClick={() => nav(`/messages`)}
                >
                    Назад
                </button>
            </div>
        </div>
    )
}

export default MessagePage