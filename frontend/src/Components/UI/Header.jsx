import {Link} from 'react-router-dom'

import HeaderLink from './Container/HeaderLink'


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
                        <HeaderLink
                            to='/'
                            text='Главная'
                        />
                        <HeaderLink
                            to='/subscriptions'
                            text='Подписки'
                        />
                        <HeaderLink
                            to='/messages'
                            text='Сообщения'
                        />
                        <HeaderLink
                            to='/journal'
                            text='Журнал активности'
                        />
                    </nav>
                </div>
            </div>
        </div>
    )
}

export default Header