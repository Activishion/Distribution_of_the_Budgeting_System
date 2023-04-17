import Header from "./Components/UI/Header"
import Footer from "./Components/UI/Footer"
import AppRouter from "./Components/UI/Router/AppRouter"


const App = () => {
    return (
        <div className="wrapper">
            <Header />
            <AppRouter />
            <Footer />
        </div>
    )
}

export default App
