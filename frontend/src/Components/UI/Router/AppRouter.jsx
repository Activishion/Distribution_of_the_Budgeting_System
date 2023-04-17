import { Routes, Route } from "react-router-dom"

import Main from "../../Pages/Main"
import Subscriptions from "../../Pages/Subscriptions"
import Messages from "../../Pages/Messages"
import MessageId from "../../Pages/MessageId"
import Journal from "../../Pages/Journal"
import JournalId from "../../Pages/JournalId"
import Error from "../../Pages/Error"


const AppRouter = () => {
    return(
        <Routes>
            <Route exact path='/' element={<Main />} ></Route>
            <Route path='/subscriptions' element={<Subscriptions />} ></Route>
            <Route exact path='/messages' element={<Messages />} ></Route>
            <Route exact path='/messages/:id' element={<MessageId />} ></Route>
            <Route exact path='/journal' element={<Journal />} ></Route>
            <Route exact path='/journal/:id' element={<JournalId />} ></Route>
            <Route path="*" element={<Error />}></Route>
        </Routes>
    )
}

export default AppRouter