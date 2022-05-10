export interface IDevice {
  code: string;
  name: string;
  category: string;
  isON: boolean;
  _id: string;
}

export interface IRoom {
  name: string;
  _id: string;
  devices: IDevice[];
}

export interface IAuth {
  username: string;
  password: string;
}
export interface IAuth2 {
  username: string;
  password: string;
  changepassword: string;
}

export interface User {
  _id: string;
  token: string;
  username: string;
  email: string;
}
