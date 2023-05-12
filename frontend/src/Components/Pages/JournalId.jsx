import React, { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom"

import JournalService from '../API/JournalAPI'
import RecordDiv from '../UI/Container/RecordDiv'
import RecordHeader from '../UI/Container/RecordHeader'


const JournalPage = () => {
    const nav = useNavigate()
    const { id } = useParams()
    const [journalId, setJournalId] = useState([])

    async function GetJournalById(id) {
        const journalById = await JournalService.getJournalById(id)
        setJournalId(journalById.report)
    }

    useEffect(() => {
        GetJournalById(id)
    }, [])

    return(
        <div className="journalId">
            <div className="header_container">
                <div className="header_container_left">
                    <RecordDiv 
                        header='Email: '
                        text={journalId?.user}
                    />
                    <RecordDiv 
                        header='Имя ползователя: '
                        text={journalId?.full_name}
                    />
                    <RecordDiv 
                        header='Внешний пользователь: '
                        text={journalId?.external ? 'Да' : 'Нет'}
                    />
                </div>
                <div className="header_container_right">
                    <div className="container_create">
                        <RecordHeader text='Создание' />
                        <RecordDiv 
                            header='Дата создания:'
                            text={journalId.data}
                        />
                        <RecordDiv 
                            header='Добавлено через портал:'
                            text={journalId?.added_via_portal ? 'Да' : 'Нет'}
                        />
                    </div>
                    <div className="container_create">
                        <RecordHeader text='Согласование' />
                        <RecordDiv 
                            header='Решение модератора: '
                            text={
                                journalId?.moderator_is_decision
                                ? 'Согласовано'
                                : 'Не согласовано'}
                        />
                        {journalId?.moderator
                            ?<RecordDiv 
                                header='Модератор: '
                                text={journalId?.moderator}
                            />
                            :<></>
                        }
                        {journalId?.data_moderation
                            ?<RecordDiv 
                                header='Дата согласования: '
                                text={journalId?.data_moderation}
                            />
                            :<></>
                        }
                        {journalId?.comment
                            ?<RecordDiv 
                                header='Комменарий: '
                                text={journalId?.comment}
                            />
                            :<></>
                        }
                    </div>
                    
                        <div className="container_create">
                            {journalId?.date_delete
                                ?<div>
                                    <RecordHeader text='Удаление' />
                                    <RecordDiv 
                                        header='Дата удаления: '
                                        text={journalId.date_delete}
                                    />
                                </div>
                                :<></>
                            }
                            {journalId?.comment_delete
                                ?<RecordDiv 
                                    header='Комменарий: '
                                    text={journalId?.comment_delete}
                                />
                                :<></>
                            }
                        </div>
                        
                </div>
            </div>
            <div className="bottom_container">
                <button
                    className="message_button"
                    onClick={() => nav(`/journal`)}
                >
                    Назад
                </button>
            </div>
        </div>
    )
}

export default JournalPage