// Create account
let data = {name:"hoale231", password:"020301", email:"leviethoa0231@gmail.com"};

fetch("/users", {
  method: "POST",
  headers: {'Content-Type': 'application/json'}, 
  body: JSON.stringify(data)
}).then((res) => res.json()).then((data)=>{console.log(data)});

// Login
let data = {email:"leviethoa0231@gmail.com", password:"020301"};

fetch("/users/login", {
  method: "POST",
  headers: {'Content-Type': 'application/json'}, 
  body: JSON.stringify(data)
}).then((res) => res.json()).then((data)=>{console.log(data)});

// => Sau khi login có info Account
// 	active: true
// 	email: "leviethoa0231@gmail.com"
// 	name: "hoale231"
// 	token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjI2OTk0ZWEyZjY2MDc4ZjdkMTVhZWEyIn0.ze2Fmp8mRu6aMCMuDpuAg0AGcJ8BGUcg2c-lP_u4NJs"
// 	_id: "626994ea2f66078f7d15aea2"
// * Lưu lại cái token, id để dùng

// Get current user
fetch("/users/", {
  method: "GET",
  headers: {'Content-Type': 'application/json', "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjI2OTk0ZWEyZjY2MDc4ZjdkMTVhZWEyIn0.ze2Fmp8mRu6aMCMuDpuAg0AGcJ8BGUcg2c-lP_u4NJs",},
}).then((res) => res.json()).then((data)=>{console.log(data)});

// Update current user
let data = {
  name: "",
  email: "",
  password: "",
};

fetch("/users/", {
  method: "PUT",
  headers: {'Content-Type': 'application/json', "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjI2OTk0ZWEyZjY2MDc4ZjdkMTVhZWEyIn0.ze2Fmp8mRu6aMCMuDpuAg0AGcJ8BGUcg2c-lP_u4NJs",},
  body: JSON.stringify(data)
}).then((res) => res.json()).then((data) => { console.log(data) });

// Add devices
let data = {
	name: "group-project.bbc-relay",
	category: "relay",
	_id: "626994ea2f66078f7d15aea2"
};

fetch("/devices/create", {
  method: "POST",
  headers: {'Content-Type': 'application/json', "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjI2OTk0ZWEyZjY2MDc4ZjdkMTVhZWEyIn0.ze2Fmp8mRu6aMCMuDpuAg0AGcJ8BGUcg2c-lP_u4NJs",}, 
  body: JSON.stringify(data)
}).then((res) => res.json()).then((data)=>{console.log(data)});

// Time used

let data = {
	name: "group-project.bbc-relay",
	start_time: "2022-04-27T00:00:00Z",
	end_time: "2022-04-29T00:00:00Z"
};
fetch("/devices/data", {
  method: "POST",
  headers: {'Content-Type': 'application/json', "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjI2OTk0ZWEyZjY2MDc4ZjdkMTVhZWEyIn0.ze2Fmp8mRu6aMCMuDpuAg0AGcJ8BGUcg2c-lP_u4NJs",},
	body: JSON.stringify(data)
}).then((res) => res.json()).then((data)=>{console.log(data)});












