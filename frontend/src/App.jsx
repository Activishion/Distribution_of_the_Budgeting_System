import Header from "./components/Header"
import Footer from "./components/Footer"
import AppRouter from "./components/UI/AppRouter"


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
