import { useState, useEffect } from "react"
import axios from 'axios'

import Dirty from "../Container/Dirty"
import PushReportContainer from '../Container/PushReportContainer'
import ButtonSubmitForm from "../Buttom/ButtonSubmitForm"
import LabelForSelectIsNull from "../Container/LabelForSelectIsNull"
import LabelForSelectIsNotNull from "../Container/LabelForSelectIsNotNull"
import OptionsForSelect from "../Container/OptionsForSelect"


const NewNews = ({ apiPort }) => {
    const [emailNews, setEmailNews] = useState('')
    const [subscriptionNews, setSubscriptionNews] = useState('')
    const [fullName, setFullName] = useState('')

    const [emailDirtyNews, setEmailDirtyNews] = useState(false)
    const [subscriptionDirtyNews, setSubscriptionDirtyNews] = useState(false)
    const [fullNameDirtyNews, setFullNameDirtyNews] = useState(false)

    const [emailErrorNews, setEmailErrorNews] = useState('Некорректный email')
    const [subscriptionErrorNews, setSubscriptionErrorNews] = useState('Выберите подписку')
    const [fullNameErrorNews, setFullNameErrorNews] = useState('Введите ФИО')

    const [statusSubmitFormNews, setStatusSubmitFormNews] = useState('')
    const [formValidNews, setFormValidNews] = useState(false)

    const handleNewsSubmit = (e) => {
        e.preventDefault()
        axios({
            method: 'POST',
            url: `http://localhost:${apiPort}/api/v1/service/news/`,
            data: {
                user: emailNews,
                subscription: subscriptionNews,
                full_name: fullName
            },
            headers: {'Content-Type': 'application/json'}
        })
        .then((response) => {
            if (response.data['status'] === 201) {
                setStatusSubmitFormNews(201)
            }
        }).catch((error) => {
            setStatusSubmitFormNews(404)
        })
        setSubscriptionNews('')
        setEmailNews('')
        setFullName('')
    }

    const emailHandlerNews = (e) => {
        setEmailNews(e.target.value)
        const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
        if (!re.test(String(e.target.value).toLowerCase())) {
            setEmailErrorNews('Некорректный email')
        } else {
            setEmailErrorNews('')
        }
    }

    const subscriptionHandlerNews = (e) => {
        setSubscriptionNews(e.target.value)
        if (!e.target.value) {
            setSubscriptionErrorNews('Выберите подписку')
        } else {
            setSubscriptionErrorNews('')
        }
    }

    const fullNameHandlerNews = (e) => {
        setFullName(e.target.value)
        if (!e.target.value) {
            setFullNameErrorNews()
        } else {
            setFullNameErrorNews('')
        }
    }

    const blurHandlerNews = (e) => {
        switch (e.target.name) {
            case 'emailNews':
                setEmailDirtyNews(true)
                break
            case 'subscriptionNews':
                setSubscriptionDirtyNews(true)
                break
            case 'fullName':
                setFullNameDirtyNews(true)
                break
        }
    }

    useEffect(() => {
        if (emailErrorNews || subscriptionErrorNews || fullNameErrorNews) {
            setFormValidNews(false)
        } else {
            setFormValidNews(true)
        }
    }, [emailErrorNews, subscriptionErrorNews, fullNameErrorNews])

    return (
        <form onSubmit={handleNewsSubmit}>
            <div className="forms">
                <p className="heade_form">Новости</p>
                <Dirty
                    className='dirtyFioNews'
                    dirty={fullNameDirtyNews}
                    error={fullNameErrorNews}
                />
                <div className="input-group">
                    <input
                        type="text"
                        id='fullName'
                        name="fullName"
                        value={fullName}
                        onChange={(e) => fullNameHandlerNews(e)}
                        onBlur={e => blurHandlerNews(e)}
                        placeholder=" "
                    />
                    <label htmlFor='fullName'>ФИО</label>
                </div>
                <Dirty
                    className='dirtyReportNews'
                    dirty={emailDirtyNews}
                    error={emailErrorNews}
                />
                <div className="input-group">
                    <input
                        type="text"
                        id='email'
                        name="emailNews"
                        value={emailNews}
                        onChange={(e) => emailHandlerNews(e)}
                        onBlur={e => blurHandlerNews(e)}
                        placeholder=" "
                    />
                    <label htmlFor='email'>Email</label>
                </div>
                <Dirty
                    className='dirtyReportNews'
                    dirty={subscriptionDirtyNews}
                    error={subscriptionErrorNews}
                />
                <div className="input-group">
                    <select
                        type="text"
                        id='reportNews'
                        name="subscriptionNews"
                        value={subscriptionNews}
                        onChange={(e) => subscriptionHandlerNews(e)}
                        onBlur={e => blurHandlerNews(e)}
                        placeholder=" "
                    >
                        <OptionsForSelect />
                    </select>
                    <LabelForSelectIsNull
                        subscription={subscriptionNews}
                        text='Подписка'
                    />
                    <LabelForSelectIsNotNull
                        subscription={subscriptionNews}
                        text='Подписка'
                    />
                </div>
                <ButtonSubmitForm valid={formValidNews} />
                <PushReportContainer statusSubmit={statusSubmitFormNews} />
            </div>
        </form>
    )
}

export default NewNews