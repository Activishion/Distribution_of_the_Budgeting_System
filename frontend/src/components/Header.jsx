import {Link} from 'react-router-dom'


const Header = () => {
    return (
        <div className='header'>
            <div className="container">
                <div>
                    <Link
                        to="/"
                        className="nav__link first"
                    >
                        <img 
                            src='Логотип_компании_«Ростелеком».png'
                            className='logo'
                            alt='Логотип'
                        />
                    </Link>
                </div>
                <div className="header__inner">
                    <nav>
                        <Link
                            to="/"
                            className="nav__link first"
                        >
                            Главная
                        </Link>
                        <Link
                            to="/subscriptions"
                            className="nav__link first"
                        >
                            Подписки
                        </Link>
                        <Link
                            to="/messages"
                            className="nav__link first"
                        >
                            Сообщения
                        </Link>
                        <Link
                            to="/journal"
                            className="nav__link first"
                        >
                            Журнал активности
                        </Link>
                    </nav>
                </div>
            </div>
        </div>
    )
}

export default Header