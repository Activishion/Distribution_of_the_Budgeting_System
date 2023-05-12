export default class PaginationService {
    static getPageCount = (totalCount, limit) => {
        return Math.ceil(totalCount / limit)
    }

    static getPagesArray = (totalPages) => {
        let result = []
        for (let i = 0; i < totalPages; i++) {
            result.push(i + 1)
        }
        return result
    }
}