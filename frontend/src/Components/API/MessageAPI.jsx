import axios from 'axios'


export default class MessageService {
    static async getAllMessages(limit = 10, page = 1) {
        const response = await axios
            .get(`http://0.0.0.0:8000/api/v1/messages`, {
                params: {
                    limit: limit,
                    page: page
                },
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }

    static async getMessageById(id) {
        const response = await axios
            .get(`http://0.0.0.0:8000/api/v1/messages/` + id, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }
}