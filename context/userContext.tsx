import React, { Component, useState } from 'react'
import { User } from '../models/models'
import { RootStackScreenProps } from '../types'


export const UserContext = React.createContext({ user: {}, setUser: (user: User) => { } })

export const user = {
    _id: "",
    username: "",
    email: "",
    token: ""
}



// export function UserProvider({}: RootStackScreenProps<"UserProvider">) {
//     const UserContext = React.createContext({})
//     const [user, setUser] = useState<User>({
//         _id: "",
//         token: "",
//         username: "",
//         email: ""
//     })

//     return <UserContext.Provider value={{user: user}}></UserContext.Provider>
// };
