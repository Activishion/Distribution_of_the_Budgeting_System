import InputSubscription from '../UI/InputSubscription'
import RadioInputSubscription from '../UI/RadioInputSubscription'
import ButtonForm from '../UI/ButtonForm'


const Subscriptions = () => {

    return (
        <div className="subscriptions">
            <div className="container_forms">
                <form action="" method="POST" id="news">
                    <div className="forms">
                        <p className="heade_form">Новости</p>
                        <InputSubscription
                            id='name'
                            htmlFor='name'
                            text='Имя пользователя'
                        />
                        <InputSubscription
                            id='email'
                            htmlFor='nemailame'
                            text='Email'
                        />
                        <div className="container">
                            <div className="radio_container">
                                <RadioInputSubscription
                                    id='radio_news_1'
                                    htmlFor='radio_news_1'
                                    text='Подписаться'
                                    name='radio_news'
                                />
                                <RadioInputSubscription
                                    id='radio_news_2'
                                    htmlFor='radio_news_2'
                                    text='Отписаться'
                                    name='radio_news'
                                />
                            </div>
                        </div>
                        <ButtonForm form='news' />
                    </div>
                </form>
                <form action="" method="POST" id="bafs">
                    <div className="forms">
                        <p className="heade_form">Отчетность БЭФС</p>
                        <InputSubscription
                            id='report'
                            htmlFor='report'
                            text='Отчет'
                            list='reports'
                        />

                        <datalist id="reports">
                            <option value="Firefox" />
                            <option value="Google Chrome" />
                            <option value="Opera" />
                            <option value="Safari" />
                        </datalist>

                        <InputSubscription
                            id='email'
                            htmlFor='nemailame'
                            text='Email'
                        />
                        <div className="container">
                            <div className="radio_container">
                                <RadioInputSubscription
                                    id='radio_bafs_1'
                                    htmlFor='radio_bafs_1'
                                    text='Подписаться'
                                    name='radio_news'
                                />
                                <RadioInputSubscription
                                    id='radio_bafs_2'
                                    htmlFor='radio_bafs_2'
                                    text='Отписаться'
                                    name='radio_news'
                                />
                            </div>
                        </div>
                        <ButtonForm form='bafs' />
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Subscriptions