import axios from 'axios'


export default class MessageService {
    static async getAllMessages(limit = 10, page = 1) {
        const response = await axios
            .get(`http://localhost:1337/api/v1/service/messages`, {
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
            .get('http://localhost:1337/api/v1/service/messages/' + id, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }
}