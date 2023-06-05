const blob = document.getElementById('blob');
document.addEventListener('mousemove', (e) => {

    blob.animate({
        left: `${(e.clientX + 50)}px`,
        top: `${e.clientY}px`
    }, {duration: 1500, fill: "forwards"});

});