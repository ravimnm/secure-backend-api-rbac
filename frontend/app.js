const API = "http://127.0.0.1:8000/api/v1"

async function register(){

const res = await fetch(API + "/auth/register",{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({
name:document.getElementById("name").value,
email:document.getElementById("email").value,
password:document.getElementById("password").value
})
})

const data = await res.json()

document.getElementById("message").innerText = data.message

// redirect to login
setTimeout(()=>{
window.location="login.html"
},1000)

}


async function login(){

const res = await fetch(API + "/auth/login",{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({
email:document.getElementById("email").value,
password:document.getElementById("password").value
})
})

const data = await res.json()

if(data.access_token){

localStorage.setItem("token",data.access_token)

// redirect to dashboard
window.location="dashboard.html"

}else{
document.getElementById("message").innerText="Login failed"
}

}


async function createTask(){

const token = localStorage.getItem("token")

await fetch(API + "/tasks",{
method:"POST",
headers:{
"Content-Type":"application/json",
"Authorization":"Bearer "+token
},
body:JSON.stringify({
title:document.getElementById("title").value,
description:document.getElementById("description").value
})
})

loadTasks()

}


async function loadTasks(){

const token = localStorage.getItem("token")

// if not logged in
if(!token){
window.location="login.html"
return
}

const res = await fetch(API + "/tasks",{
headers:{
"Authorization":"Bearer "+token
}
})

const tasks = await res.json()

const list = document.getElementById("tasks")

list.innerHTML=""

tasks.forEach(task=>{
const li = document.createElement("li")
li.innerText = task.title + " - " + task.status
list.appendChild(li)
})

}


function logout(){

localStorage.removeItem("token")

window.location="login.html"

}