const heartEffect = (id) => {
    id.classList.toggle("is-active");
    setTimeout(() => {
        id.classList.toggle("is-active");
    }, 3000);
}
const swalLoginEffect = () => {
    swal({
        title: "로그인이 필요한 기능입니다.",
        icon: "warning",
        buttons: "로그인하기"
    }).then((value) => {
        if (value) {
            location.href = "/users/login"
        }
    })
}