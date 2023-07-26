import NewReport from '../UI/Form/NewReport'
import NewNews from '../UI/Form/NewNews'


const Subscriptions = ({ apiPort }) => {

    return (
        <div className="subscriptions">
            <div className="container_forms">
                <NewReport apiPort={apiPort} />
                <NewNews apiPort={apiPort} />
            </div>
        </div>
    )
}

export default Subscriptions