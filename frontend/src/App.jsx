import Header from "./Components/UI/Header"
import Footer from "./Components/UI/Footer"
import AppRouter from "./Components/UI/Router/AppRouter"


const App = () => {
    const apiPort = 1337

    return (
        <div className="wrapper">
            <Header />
            <AppRouter apiPort={apiPort}/>
            <Footer />
        </div>
    )
}

export default App
