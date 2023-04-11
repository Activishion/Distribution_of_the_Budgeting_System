const Subscriptions = () => {
    return (
        <div className="subscriptions">
            <p className="subscriptions_header">
                Теперь у нас появилась возможность подписаться и отписаться от рассылки 
                новостей Системы бюджетирования и от рассылаемых версий интерактивной 
                отчетности БЭФС в одной форме.
            </p>
            <div className="forms">
                <div class="input-group">
                    <input type="text" id="name" placeholder=" " />
                    <label for="name">Имя пользователя</label>
                </div>
                <div class="input-group">
                    <input type="text" id="email" placeholder=" " />
                    <label for="email">Email</label>
                </div>
                <div class="input-group">
                    <input type="text" id="report" placeholder=" " />
                    <label for="report">Отчет</label>
                </div>
                <div className="description_input">
                    {/* <div className="switch">
                        <input type="checkbox" class="switch" id="switch" />
                        <label for="switch" class="label">slide to unlock</label>
                    </div> */}
                </div>
            </div>
        </div>
    )
}

export default Subscriptions