function showPage(page){

let pages=document.querySelectorAll(".page")

pages.forEach(p=>p.classList.remove("active"))

document.getElementById(page).classList.add("active")

}

function loadLesson(topic){

fetch("/lesson/"+topic)
.then(res=>res.json())
.then(data=>{

document.getElementById("lessonTitle").innerText = data.title

document.getElementById("lessonText").innerHTML = data.text

})

}