function blinkText() {
    const terminalBlink = document.querySelector('.terminalBlink');
    terminalBlink.style.opacity = terminalBlink.style.opacity === '1' ? '0' : '1';
}

setInterval(blinkText, 500);