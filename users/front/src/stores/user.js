import { defineStore } from "pinia";
import userService from '@/api/user'

export const useUserStore = defineStore('user', {
    state: () => {
        return{
            users: []
        }
    },
    actions: {
        async getUsers(){
            try {
                const data = await userService.getUsers()
                this.users = data;
            } catch (error) {
                console.log(error)
            }
        },
        async addUser(user){
            try {
                const data = await userService.addUser(user)
                this.getUsers()
            } catch (error) {
                console.log(error)
            }
        }
    }
})