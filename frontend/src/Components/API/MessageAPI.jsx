import axios from 'axios'


export default class MessageService {
    static async getAllMessages(limit = 10, page = 1, apiPort) {
        const response = await axios
            .get(`http://localhost:${apiPort}/api/v1/service/messages`, {
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

    static async getMessageById(id, apiPort) {
        const response = await axios
            .get(`http://localhost:${apiPort}/api/v1/service/messages/` + id, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }
}