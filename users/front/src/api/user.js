import axios from 'axios'

class UserService {
    async getUsers() {
        const { data } = await axios.get('/usuarios/')
        console.log(data)
        return data;
    }
    async addUser(user) {
        const { data } = await axios.post('/usuarios/', user)
        return data;
    }
}

export default new UserService();