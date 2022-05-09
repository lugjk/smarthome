export interface IDivice {
  code: string;
  name: string;
  type: string;
  isON: boolean;
  time6: number;
  time12: number;
  time18: number;
  time24: number;
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
