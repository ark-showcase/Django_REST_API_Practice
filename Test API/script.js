/* //GET Request
axios.get("http://127.0.0.1:8000/apiV1/status/list/")
    .then(response => console.log(response))

//Detail Request
axios.get("http://127.0.0.1:8000/apiV1/status/detail/6/")
    .then(response => console.log(response))

// POST Request
let status = {
    user: 8,
    content: "Testing API",
    image: null
}
axios.post("http://127.0.0.1:8000/apiV1/status/create/", status, {
    headers: {
        "Content-Type": "application/json"
    }
})
    .then(response => console.log(response))
    .catch(error => console.log(error.message))

//Delete Request
axios.delete("http://127.0.0.1:8000/apiV1/status/delete/5/")
    .then(response => console.log(response))
    .catch(error => console.log(error.message))

// PUT Request
let sts = {
    user: 1,
    content: "Updated Testing API!",
    image: null
}
axios.put("http://127.0.0.1:8000/apiV1/status/update/6/", sts, {
    headers: {
        "Content-Type": "application/json"
    }
})
    .then(response => console.log(response))
    .catch(error => console.log(error.message))

// PATCH Request
let stss = {
    content: "Updated Testing API! using PATCH",
}
axios.patch("http://127.0.0.1:8000/apiV1/status/update/4/", stss, {
    headers: {
        "Content-Type": "application/json"
    }
})
    .then(response => console.log(response))
    .catch(error => console.log(error.message)) */


document.getElementById('myForm').addEventListener('submit', handleSubmit);
document.getElementById('image').addEventListener('change', handleImage);

let myImage = null;

function handleImage(e){
    myImage = e.target.files[0];
    console.log(myImage);
}

function handleSubmit(e){
    e.preventDefault();
    let user = document.getElementById('user').value;
    let content = document.getElementById('content').value;
    let form_data = new FormData();
    form_data.append('user', user);
    form_data.append('content', content);
    form_data.append('image', myImage);

    /* for(var [key, value] of form_data.entries()){
        console.log(key, ": ", value);
    } */
    axios.put("http://127.0.0.1:8000/apiV1/status/10/", form_data, {
        header: {
            "Content-Type": "multipart/form-data"
        }
    })
        .then(response => response.data)
        .then(data => console.log(data))
}