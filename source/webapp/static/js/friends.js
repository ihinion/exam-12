async function onAddFriend(event) {
    event.preventDefault();
    let addFriendBtn = event.target
    let url = addFriendBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
    }
    catch (error) {
        console.log(error)
    }
    addFriendBtn.classList.add('hidden');
    console.log('hidden')
    const unFriendBtn = addFriendBtn.parentElement.getElementsByClassName('un-friend')[0];
    console.log('no class')
    unFriendBtn.classList.remove('hidden');
}


async function onUnFriend(event) {
    event.preventDefault();
    let unFriendBtn = event.target;
    let url = unFriendBtn.href;

    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
    }
    catch (error) {
        console.log(error);
    }

    unFriendBtn.classList.add('hidden');
    const addFriendBtn = unFriendBtn.parentElement
        .getElementsByClassName('add-friend')[0];
    addFriendBtn.classList.remove('hidden');
}

window.addEventListener('load', function () {
    const addFriendButtons = document.getElementsByClassName('add-friend');
    const unFriendButtons = document.getElementsByClassName('un-friend');
    for (let btn of addFriendButtons) {btn.onclick = onAddFriend}
    for (let btn of unFriendButtons) {btn.onclick = onUnFriend}
});