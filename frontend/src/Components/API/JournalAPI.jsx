import axios from 'axios'


export default class JournalService {
    static async getAllJournals(limit = 10, page = 1) {
        const response = await axios
            .get(`http://127.0.0.1:8000/api/v1/service/report?limit=${limit}`, {
                params: {
                    _limit: limit,
                    _page: page
                }
            })
        return response.data.reports
    }

    static async getJournalById(id) {
        const response = await axios
            .get('http://127.0.0.1:8000/api/v1/service/report/' + id, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data.report
    }
}