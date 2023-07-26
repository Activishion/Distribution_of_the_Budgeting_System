import axios from 'axios'


export default class JournalService {
    static async getAllJournals(limit = 10, page = 1, apiPort) {
        const response = await axios
            .get(`http://localhost:${apiPort}/api/v1/service/report`, {
                params: {
                    limit: limit,
                    page: page
                }
            })
        return response.data
    }

    static async getJournalById(id, apiPort) {
        const response = await axios
            .get(`http://localhost:${apiPort}/api/v1/service/report/` + id, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }
}