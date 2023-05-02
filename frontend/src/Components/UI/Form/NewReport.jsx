import { useState } from "react"
import axios from 'axios'


const NewReport = () => {
    const [report, setReport] = useState('')
    const [email, setEmail] = useState('')
    const [subscription, setSubscription] = useState('')

    const handleReportSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/v1/service/report/', {
            report: report,
            email: email,
            subscription: subscription
        })
        .then((response) => {
            console.log(response.data)
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <form onSubmit={handleReportSubmit}>
            <div className="forms">
                <p className="heade_form">Отчетность БЭФС</p>
                <div className="input-group">
                    <input
                        type="text"
                        id='report'
                        list='report'
                        value={report}
                        onChange={(e) => setReport(e.target.value)}
                        placeholder=" "
                    />
                    <label htmlFor='report'>Отчет</label>
                </div>

                <datalist id="report">
                    <option value="Прибыли и убытки РТК" />
                    <option value="РТК + Tele2" />
                    <option value="Сегментная отчетность" />
                </datalist>

                <div className="input-group">
                    <input
                        type="text"
                        id='email'
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder=" "
                    />
                    <label htmlFor='email'>Email</label>
                </div>
                <div className="input-group">
                    <input
                        type="text"
                        id='subscription'
                        list='subscriptionReport'
                        onChange={(e) => setSubscription(e.target.value)}
                        value={subscription}
                        placeholder=" "
                    />
                    <label htmlFor='subscription'>Подписка</label>
                </div>

                <datalist id="subscriptionReport">
                    <option value="Подписаться" />
                    <option value="Отписаться" />
                </datalist>

                <div className="container_button">
                    <button type="submit">
                        Отправить
                    </button>
                </div>
            </div>
        </form>
    )
}

export default NewReport