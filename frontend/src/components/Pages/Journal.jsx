const Journal = () => {
    return (
        <div className="journal">
            <h1 className="journal_header">
                Изменение списка рассылки за последние 30 дней
            </h1>
            <div className="container">
                <table rules="groups">
                    <thead>
                        <tr>
                            <th>Дата</th>
                            <th>Изменение</th>
                            <th>Статус</th>
                            <th>Email</th>
                            <th>Пользователь</th>
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

export default Journal