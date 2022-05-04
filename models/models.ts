export interface IDivice {
  code: string;
  name: string;
  type: string;
  isON: boolean;
  id: number;
}

export interface IRoom {
  title: string;
  id: number;
  divices: IDivice[];
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
