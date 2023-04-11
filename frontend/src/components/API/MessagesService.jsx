import axios from 'axios'


export default class MessageService {
    static async getAllMessages(limit = 10, page = 1) {
        const response = await axios.get('юрл ссылки сообщений', {
            params: {
                _limit: limit,
                _page: page
            }
        })
        return response
    }

    static async getMessageById(id) {
        const response = await axios.get('юрл ссылки сообщений' + id)
        return response
    }
}