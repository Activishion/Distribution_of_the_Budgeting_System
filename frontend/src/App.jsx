import { BrowserRouter, Routes, Route } from "react-router-dom"

import Header from "./components/Header"
import Footer from "./components/Footer"
import Main from "./components/Pages/Main"
import Subscriptions from "./components/Pages/Subscriptions"
import Messages from "./components/Pages/Messages"
import Journal from "./components/Pages/Journal"


const App = () => {
    return (
        <div className="wrapper">
            <BrowserRouter>
                <Header />
                <Routes>
                    <Route path='/' element={<Main />} ></Route>
                    <Route path='/subscriptions' element={<Subscriptions />} ></Route>
                    <Route path='/messages' element={<Messages />} ></Route>
                    <Route path='/journal' element={<Journal />} ></Route>
                </Routes>
                <Footer />
            </BrowserRouter>
        </div>
    )
}

export default App
