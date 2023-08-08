import axios from 'axios' 

export default class producerApi {
    async createUser(user) {
        const {data} = await axios.post('api/usuarios/', user)
        return data
    }
}