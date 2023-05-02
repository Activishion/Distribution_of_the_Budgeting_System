import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"

import JournalService from '../API/JournalAPI'


const Journal = () => {
    const nav = useNavigate()

    const [journal, setJournal] = useState([])

    async function GetJournals(limit = 10, page = 1) {
        const allJournal = await JournalService.getAllJournals(limit, page)
        setJournal(allJournal)
    }

    useEffect(() => {
        GetJournals()
    }, [])

    return (
        <div className="journal">
            <h1 className="journal_header">
                Изменение списка рассылки за последние 30 дней
            </h1>
            <div className="container">
                <table rules="groups">
                    <thead>
                        <tr>
                            <th>Дата</th>
                            <th>Изменение</th>
                            <th>Статус</th>
                            <th>Email</th>
                            <th>Пользователь</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {journal.map(record => (
                            <tr key={record.id}>
                                <td>{record.data}</td>
                                <td>
                                    {record.subscription
                                    ? 'Включение'
                                    : 'Исключение'
                                    }
                                </td>
                                <td>
                                    {record?.user?.moderator_is_decision
                                    ? 'Согласовано'
                                    : 'Ожидает'
                                    }
                                </td>
                                <td>{record.email}</td>
                                <td>{record.full_name}</td>
                                <td className="last_td">
                                    <button 
                                        className="buttom_table"
                                        onClick={() => nav(`/journal/${record.id}`)}
                                    >
                                        Подробнее
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default Journal