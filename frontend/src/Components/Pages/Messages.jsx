import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"
import axios from 'axios'


const Messages = () => {
    const nav = useNavigate()
    const [messages, setMessages] = useState([])

    async function GetMessages(limit = 10, page = 1) {
        const response = await axios.get('юрл ссылки сообщений', {
            params: {
                _limit: limit,
                _page: page
            }
        })
        setMessages(response.data)
    }

    useEffect(() => {
        GetMessages()
    }, [])

    return (
        <div className="message">
            <h1 className="message_header">Архив сообщений за последний год</h1>
            <div className="container">
                <table rules="groups">
                    <thead>
                        <tr>
                            <th>Дата</th>
                            <th>ПАО</th>
                            <th>ДЗО</th>
                            <th>Тема</th>
                            <th>Сообщение</th>
                            <th>Автор</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {messages.map(message => 
                            <tr>
                                <td>{message.date}</td>
                                <td>{message.PAO}</td>
                                <td>{message.DZO}</td>
                                <td>{message.subject}</td>
                                <td>{message.message}</td>
                                <td>{message.author}</td>
                                <td className="last_td">
                                    <button 
                                        className="buttom_table"
                                        onClick={() => nav(`/messages/${message.id}`)}
                                    >
                                        Подробнее
                                    </button>
                                </td>
                            </tr>
                        )}
                        <tr>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td className="last_td">
                                <button 
                                    className="buttom_table"
                                    onClick={() => nav(`/messages/1`)}  // Заменить на динамическую ссылку
                                >
                                    Подробнее
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default Messages