


const Messages = () => {
    return (
        <div className="message">
            <h1 className="message_header">Архив сообщений за последний год</h1>
            <div className="container">
                <table rules="groups">
                    <thead>
                        <tr>
                            <th>Дата</th>
                            <th>ПАО</th>
                            <th>ДЗО</th>
                            <th>Тема</th>
                            <th>Сообщение</th>
                            <th>Автор</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td>Ячейка</td>
                            <td className="last_td">
                                <button className="buttom_table">Подробнее</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default Messages