import {BrowserRouter, Link} from 'react-router-dom'


const Header = () => {
    return (
        <BrowserRouter>
            <div className='header'>
                <div className="container">
                    <div>
                        <img 
                            src='Логотип_компании_«Ростелеком».png'
                            className='logo'
                            alt='Логотип'
                        />
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
                                to="/distributed_reports"
                                className="nav__link first"
                            >
                                Подписки
                            </Link>
                            <Link
                                to="/message_archive"
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
        </BrowserRouter>
    )
}

export default Header