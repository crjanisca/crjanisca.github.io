fetch('https://www.myteklab.com/APIV1/loginDetails').then(function(response) {
    response.json().then(function(data) {
        document.getElementById('student_name').innerHTML = data.login_first_name;
        document.getElementById('student_profile_picture').innerHTML = data.profile_picture;
        document.getElementById('student_likes').innerHTML = data.total_likes;
    })
})