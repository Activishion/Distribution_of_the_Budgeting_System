import { useState } from "react"
import { getPageCount } from "./Pages"


const Pagination = () => {
    const [totaPage, setTotalPage] = useState(0)
    const [limit, setLimit] = useState(10)
    const [page, setPage] = useState(1)

    const totalCount = response.headers['x-total-count']
    setTotalPage(getPageCount(totalCount, limit))
}