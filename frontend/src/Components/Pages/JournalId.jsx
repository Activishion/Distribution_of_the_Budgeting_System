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
        setJournalId(journalById)
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
                        text={journalId?.user?.email}
                    />
                    <RecordDiv 
                        header='Имя ползователя: '
                        text={journalId?.user?.full_name}
                    />
                    <RecordDiv 
                        header='Внешний пользователь: '
                        text={journalId?.user?.external ? 'Да' : 'Нет'}
                    />
                </div>
                <div className="header_container_right">
                    <div className="container_create">
                        <RecordHeader text='Создание' />
                        <RecordDiv 
                            header='Дата создания:'
                            text={journalId?.user?.date_create}
                        />
                        <RecordDiv 
                            header='Добавлено через портал:'
                            text={journalId?.user?.added_via_portal ? 'Да' : 'Нет'}
                        />
                    </div>
                    <div className="container_create">
                        <RecordHeader text='Согласование' />
                        <RecordDiv 
                            header='Решение модератора: '
                            text={
                                journalId?.user?.moderator_is_decision
                                ? 'Согласовано'
                                : 'Не согласовано'}
                        />
                        {journalId?.user?.moderator
                            ?<RecordDiv 
                                header='Модератор: '
                                text={journalId?.user?.moderator}
                            />
                            :<></>
                        }
                        {journalId?.user?.data_moderation
                            ?<RecordDiv 
                                header='Дата согласования: '
                                text={journalId?.user?.data_moderation}
                            />
                            :<></>
                        }
                        {journalId?.user?.comment
                            ?<RecordDiv 
                                header='Комменарий: '
                                text={journalId?.user?.comment}
                            />
                            :<></>
                        }
                    </div>
                    
                        <div className="container_create">
                            {journalId?.user?.date_delete
                                ?<div>
                                    <RecordHeader text='Удаление' />
                                    <RecordDiv 
                                        header='Дата удаления: '
                                        text={journalId?.user?.date_delete}
                                    />
                                </div>
                                :<></>
                            }
                            {journalId?.user?.comment_delete
                                ?<RecordDiv 
                                    header='Комменарий: '
                                    text={journalId?.user?.comment_delete}
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