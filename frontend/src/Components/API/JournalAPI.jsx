import axios from 'axios'


export default class JournalService {
    static async getAllJournals(limit = 10, page = 1) {
        const response = await axios
            .get(`http://127.0.0.1:8000/api/v1/reports`, {
                params: {
                    limit: limit,
                    page: page
                }
            })
        return response.data
    }

    static async getJournalByEmail(email) {
        const response = await axios
            .get(`http://127.0.0.1:8000/api/v1/reports/` + email, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }

    static async getListReports() {
        const response = await axios
            .get(`http://127.0.0.1:8000/api/v1/list_reports_for_subscription`, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        return response.data
    }
}