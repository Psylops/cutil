const blob = document.getElementById('blob');
let bWidth = blob.style.width / 2;
let bHeight = blob.style.height / 2;
document.addEventListener('mousemove', (e) => {
    let bX = e.clientX - bWidth;
    let bY = e.clientY - bHeight;
    blob.animate({
        left: `${bX}px`,
        top: `${bY}px`
    }, {duration: 1500, fill: "forwards"});

});