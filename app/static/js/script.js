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