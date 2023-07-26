import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"

import MessageService from '../API/MessageAPI'
import PaginationService from '../UI/Pagination/Pages'


const Messages = () => {
    const nav = useNavigate()
    const [messages, setMessages] = useState([])
    const [totalPages, setTotalPages] = useState(0)
    const [limit, ] = useState(10)
    const [page, setPage] = useState(1)
    // console.log(messages)
    let pagesArray = PaginationService.getPagesArray(totalPages)

    async function GetMessages() {
        const allMessages = await MessageService.getAllMessages(limit, page)
        const totalCount = allMessages.count
        setMessages(allMessages.results.message)
        if (totalCount > 10) {
            setTotalPages(PaginationService.getPageCount(totalCount, limit))
        }
    }

    const changePage = (p) => {
        setPage(p)
    }

    useEffect(() => {
        GetMessages()
    }, [page])

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
                            <tr key={message.id}>
                                <td>{message.date}</td>
                                <td>{message.PAO ? 'Да' : 'Нет'}</td>
                                <td>{message.DZO ? 'Да' : 'Нет'}</td>
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
                    </tbody>
                </table>
            </div>
            <div className="pagination">
                {pagesArray.map(p => 
                    <span 
                        key={p}
                        onClick={() => changePage(p)}
                        className={page === p ? 'page_active' : 'page'}
                    >
                        <p>{p}</p>
                    </span>
                )}
            </div>
        </div>
    )
}

export default Messages