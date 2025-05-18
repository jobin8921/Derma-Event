function handle3D(e, element) {
    const rect = element.getBoundingClientRect();
    const x = e.clientX - rect.left; // x position within the element
    const y = e.clientY - rect.top;  // y position within the element

    const centerX = rect.width / 10;
    const centerY = rect.height / 10;

    const rotateX = -(y - centerY) / 50;
    const rotateY = (x - centerX) / 50;

    element.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
}

function reset3D(element) {
    element.style.transform = 'rotateX(0deg) rotateY(0deg)';
}
