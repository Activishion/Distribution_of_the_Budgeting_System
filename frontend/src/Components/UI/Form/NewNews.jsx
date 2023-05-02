import { useState } from "react"
import axios from 'axios'


const NewNews = () => {
    const [email, setEmail] = useState('')
    const [subscriptionNews, setSubscriptionNews] = useState('')

    const handleNewsSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/v1/service/news/', {
            email: email,
            subscription: subscriptionNews
        })
        .then((response) => {
            console.log(response.data)
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <form onSubmit={handleNewsSubmit}>
            <div className="forms">
                <p className="heade_form">Новости</p>
                <div className="input-group">
                    <input type="text" id='name' placeholder=" " />
                    <label htmlFor='name'>Имя пользователя</label>
                </div>
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
                        id='reportNews'
                        list='subscriptionNews'
                        value={subscriptionNews}
                        onChange={(e) => setSubscriptionNews(e.target.value)}
                        placeholder=" "
                    />
                    <label htmlFor='reportNews'>Подписка</label>
                </div>  

                <datalist id="subscriptionNews">
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

export default NewNews