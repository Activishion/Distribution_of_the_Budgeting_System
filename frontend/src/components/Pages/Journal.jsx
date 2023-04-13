import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"
import axios from 'axios'


const Journal = () => {
    const nav = useNavigate()

    const [journal, setjournal] = useState([])

    async function fetchJournal(limit = 10, page = 1) {
        const response = await axios.get('юрл ссылки журнала', {
            params: {
                _limit: limit,
                _page: page
            }
        })
        setjournal(response.data)
    }

    useEffect(() => {
        fetchJournal()
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
                        <tr>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td className="last_td">
                                <button 
                                    className="buttom_table"
                                    onClick={() => nav(`/journal/1`)}  // Заменить на динамическую ссылку
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

export default Journal