import FooterContainer from "./Container/FooterContainer"


const Footer = () => {
    return (
        <div className="footer">
            <div className="footer_content">
                <div className="footer_content_items">
                    <div className="footer_item">
                        <p className="footer_text">
                            ©2023 Создано Департаментом экономики и инвестиций для плановиков
                        </p>
                    </div>
                    <div className="footer_item">
                        <FooterContainer
                            position='Руководитель проекта: '
                            email='andrey.lisichenko@rt.ru'
                            href='mailto:andrey.lisichenko@rt.ru'
                        />
                        <FooterContainer
                            position='Техническая поддержка: '
                            email='aleksey.khaydukov@sibir.rt.ru'
                            href='mailto:aleksey.khaydukov@sibir.rt.ru'
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Footer