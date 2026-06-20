/* Atmosphere Engine Simulation Logic */

document.addEventListener('DOMContentLoaded', () => {
    const btnSnow = document.getElementById('btn-snowflakes');
    const btnBalloons = document.getElementById('btn-balloons');
    const canvas = document.getElementById('animation-canvas');

    // List of snowflake glyphs to vary the shapes
    const snowGlyphs = ['❄', '❅', '❆', '•'];

    // List of vibrant color schemes for balloons
    const balloonColors = [
        '#ff4081', // Magenta
        '#ab47bc', // Purple
        '#29b6f6', // Bright Cyan
        '#26a69a', // Teal
        '#ff7043', // Coral
        '#ffca28', // Gold
        '#ec407a'  // Pink
    ];

    // Helper to generate a random number within a range
    function randomRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    // --- SNOWFLAKE CASCADE INITIATION ---
    function startSnowfall() {
        // Disable button for 5 seconds duration
        btnSnow.disabled = true;
        btnSnow.style.opacity = '0.5';

        // Spawn 65 snowflakes with staggered delays
        const totalSnowflakes = 65;
        for (let i = 0; i < totalSnowflakes; i++) {
            createSnowflake();
        }

        // Re-enable button after 5 seconds (cascade duration)
        setTimeout(() => {
            btnSnow.disabled = false;
            btnSnow.style.opacity = '1';
        }, 5000);
    }

    function createSnowflake() {
        const flake = document.createElement('div');
        flake.classList.add('snowflake');
        
        // Randomize snowflake symbol
        flake.innerText = snowGlyphs[Math.floor(Math.random() * snowGlyphs.length)];
        
        // Physics randomization via CSS variables
        const size = randomRange(10, 26) + 'px';
        const opacity = randomRange(0.4, 1.0);
        const duration = randomRange(3.0, 5.0) + 's';
        const delay = randomRange(0, 1.8) + 's';
        const drift = randomRange(-40, 40) + 'px';
        const startLeft = randomRange(0, 100) + '%';

        flake.style.setProperty('--size', size);
        flake.style.setProperty('--opacity', opacity);
        flake.style.setProperty('--duration', duration);
        flake.style.setProperty('--delay', delay);
        flake.style.setProperty('--drift', drift);
        flake.style.left = startLeft;

        // Auto cleanup on animation completion
        flake.addEventListener('animationend', () => {
            flake.remove();
        });

        canvas.appendChild(flake);
    }

    // --- BALLOON ASCENT INITIATION ---
    function startBalloonAscent() {
        // Disable button for 5 seconds duration
        btnBalloons.disabled = true;
        btnBalloons.style.opacity = '0.5';

        // Spawn 25 balloons with staggered delays
        const totalBalloons = 25;
        for (let i = 0; i < totalBalloons; i++) {
            createBalloon();
        }

        // Re-enable button after 5 seconds (float duration)
        setTimeout(() => {
            btnBalloons.disabled = false;
            btnBalloons.style.opacity = '1';
        }, 5000);
    }

    function createBalloon() {
        const balloon = document.createElement('div');
        balloon.classList.add('balloon');

        // Create string node
        const string = document.createElement('div');
        string.classList.add('balloon-string');
        balloon.appendChild(string);

        // Physics & appearance randomization via CSS variables
        const sizeFactor = randomRange(0.8, 1.25);
        const width = (50 * sizeFactor) + 'px';
        const height = (65 * sizeFactor) + 'px';
        const color = balloonColors[Math.floor(Math.random() * balloonColors.length)];
        const duration = randomRange(4.5, 6.0) + 's';
        const delay = randomRange(0, 1.5) + 's';
        const wobble = randomRange(-60, 60) + 'px';
        const angle = randomRange(-15, 15) + 'deg';
        const startLeft = randomRange(5, 95) + '%';

        balloon.style.setProperty('--width', width);
        balloon.style.setProperty('--height', height);
        balloon.style.setProperty('--color', color);
        balloon.style.setProperty('--duration', duration);
        balloon.style.setProperty('--delay', delay);
        balloon.style.setProperty('--wobble', wobble);
        balloon.style.setProperty('--angle', angle);
        balloon.style.left = startLeft;

        // Auto cleanup on animation completion
        balloon.addEventListener('animationend', () => {
            balloon.remove();
        });

        canvas.appendChild(balloon);
    }

    // Event Listeners
    btnSnow.addEventListener('click', startSnowfall);
    btnBalloons.addEventListener('click', startBalloonAscent);
});
