import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"

import JournalService from '../API/JournalAPI'
import PaginationService from '../UI/Pagination/Pages'


const Journal = ({ apiPort }) => {
    const nav = useNavigate()

    const [journal, setJournal] = useState([])
    const [totalPages, setTotalPages] = useState(0)
    const [limit, ] = useState(10)
    const [page, setPage] = useState(1)

    let pagesArray = PaginationService.getPagesArray(totalPages)
    
    async function GetJournals() {
        const allJournal = await JournalService.getAllJournals(limit, page, apiPort)
        const totalCount = allJournal.count
        setJournal(allJournal.results.reports)
        if (totalCount > 10) {
            setTotalPages(PaginationService.getPageCount(totalCount, limit))
        }
    }

    const changePage = (p) => {
        setPage(p)
    }

    useEffect(() => {
        GetJournals()
    }, [page])

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
                            <th>Отчет</th>
                            <th>Email</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {journal.map(record => (
                            <tr key={record.id}>
                                <td>{record.data}</td>
                                <td>
                                    {record?.subscription
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
                                <td>{record.report}</td>
                                <td>{record.user}</td>
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

export default Journal