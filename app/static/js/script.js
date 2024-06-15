function removeFlash(id) {
    const element = document.getElementById(id);
    element.remove();
}
function toggleComments(postId) {
    var commentsDiv = document.getElementById('comments-' + postId);
    if (commentsDiv.classList.contains('hidden')) {
        commentsDiv.classList.remove('hidden');
    } else {
        commentsDiv.classList.add('hidden');
    }
}

function likes(id){
    const likeButton = document.getElementById(`like-${id}`);
    const likeImg = document.getElementById(`like-img-${id}`);
    let likeCount = document.getElementById(`like-count-${id}`);
    console.log(likeCount.value)
    
    fetch(`/like/${id}`, {method: 'POST'}).then(response => response.json()).then(data => {
        if(data['liked']){
            likeImg.src = `static/svg/thumbs-up-solid.svg`;
        }
        else{
            likeImg.src = `static/svg/thumbs-up.svg`;
        }
        if(data['likes'] == 0){
            likeCount.innerHTML = "Likes";
        }
        else{
            likeCount.innerHTML = data['likes'];
        }
        console.log(data);
    });
    
}
function dislikes(id){
    const dislikeButton = document.getElementById(`dislike-${id}`);
    let dislikeCount = document.getElementById(`dislike-count-${id}`);
    const dislikeImg = document.getElementById(`dislike-img-${id}`);
    fetch(`/dislike/${id}`, {method: 'POST'}).then(response => response.json()).then(data => {
        if(data['disliked']){
            dislikeImg.src = `static/svg/thumbs-down-solid.svg`;
        }
        else{
            dislikeImg.src = `static/svg/thumbs-down.svg`;
        }
        if(data['dislikes'] == 0){
            dislikeCount.innerHTML = "Dislikes";
        }
        else{
            dislikeCount.innerHTML = data['dislikes'];
        }
        console.log(data);
    });
    
}