import React, { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom"
import axios from 'axios'

import RecordDiv from '../UI/Container/RecordDiv'
import RecordHeader from '../UI/Container/RecordHeader'


const JournalPage = () => {
    const nav = useNavigate()
    const { id } = useParams()
    const [journalId, setJournalId] = useState(null)

    async function GetJournalById(id) {
        const response = await axios.get('юрл ссылки журнала' + id)
        setJournalId(response.data)
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
                        text='тут будет почта'
                    />
                    <RecordDiv 
                        header='Имя ползователя: '
                        text='Анатолий белкин'
                    />
                    <RecordDiv 
                        header='Внешний пользователь: '
                        text='Нет'
                    />
                </div>
                <div className="header_container_right">
                    <div className="container_create">
                        <RecordHeader text='Создание' />
                        <RecordDiv 
                            header='Дата создания:'
                            text='тут будет дата создания'
                        />
                        <RecordDiv 
                            header='Добавлено через портал:'
                            text='Да'
                        />
                    </div>
                    <div className="container_create">
                        <RecordHeader text='Согласование' />
                        <RecordDiv 
                            header='Решение модератора: '
                            text='Согласовано'
                        />
                        <RecordDiv 
                            header='Модератор: '
                            text='Лисиченко Андрей Валерьевич'
                        />
                        <RecordDiv 
                            header='Дата согласования: '
                            text='11:11 13.12.13'
                        />
                        <RecordDiv 
                            header='Комменарий: '
                            text='Тут пишем своим комменты'
                        />
                    </div>
                    <div className="container_create">
                        <RecordHeader text='Удаление' />
                        <RecordDiv 
                            header='Дата удаления: '
                            text='11:11 13.12.13'
                        />
                        <RecordDiv 
                            header='Комменарий: '
                            text='Тут пишем своим комменты'
                        />
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