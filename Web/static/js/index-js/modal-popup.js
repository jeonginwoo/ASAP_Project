
const modal = document.getElementById('modal');
const scribe_button = document.getElementById('scribe');
const close_button_up = modal.querySelector('.btn-close');
const close_button_down = modal.querySelector('.btn-secondary');
const modal_image = modal.querySelector('.image');
const modal_content = modal.querySelector('.content');

let isScribe = false;

scribe_button.onclick = () => {
    if (!isScribe) isScribe = true;

    if (isScribe) {
        modal.style.display = "flex";
        image = "static/img/pubao_1.webp";

        modal_image.innerHTML = "<img src='" + image + "' style='display: block; margin: 0px auto;' width='150' height='200'/>";
        modal_content.innerHTML = "<h2>" + "푸바오 증명사진" + "</h2><hr><p>" + "귀여운 푸바오 사진이다. <br> 테스트 테스트 <br> 테스트 테스트" + "</p>";
    };
};

close_button_up.addEventListener("click", () => {
    if (isScribe) isScribe = false;

    if (!isScribe) {
        modal.style.display = "none";

        modal_image.innerHTML = "";
        modal_content.innerHTML = "";
    }
});

close_button_down.addEventListener("click", () => {
    if (isScribe) isScribe = false;

    if (!isScribe) {
        modal.style.display = "none";

        modal_image.innerHTML = "";
        modal_content.innerHTML = "";
    }
});