import React, { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import axios from 'axios'


const JournalPage = () => {
    const { id } = useParams()
    const [journalId, setJournalId] = useState(null)

    async function fetchJournalById(id) {
        const response = await axios.get('юрл ссылки журнала' + id)
        setJournalId(response.data)
    }

    useEffect(() => {
        fetchJournalById(id)
    }, [])

    return( 
        <div className="journalId">
            Страница активности
        </div>
    )
}

export default JournalPage