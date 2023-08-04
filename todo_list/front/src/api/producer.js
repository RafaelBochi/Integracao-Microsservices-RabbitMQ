import axios from 'axios' 

export default class producerApi {
    async createUser(username, password, email) {
        const {data} = await axios.post('user/', )
    }
}