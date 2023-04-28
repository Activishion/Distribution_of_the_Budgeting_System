import axios from 'axios'


export const subscriptionNews = async (email, subscription) => {
    const response = await axios
        .post('http://127.0.0.1:8000/api/v1/service/news/', {
            email,
            subscription
        })
    return response
}
