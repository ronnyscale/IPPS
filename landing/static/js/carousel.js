// $(document).ready(function() {
//     var typed = new Typed('#typing', {
//         strings: ["Приветствуем Вас", "Рады видеть Вас"],
//         typeSpeed: 50, // скорость печатания
//         backSpeed: 50, // скорость стирания
//         startDelay: 500, // задержка перед началом печатания
//         loop: false // отключаем повторение
//     });
// });

$(document).ready(function () {
    // Функция для установки флага с истечением срока действия
    function setTypedFlag() {
        var expiryTime = new Date().getTime() + (1 * 60 * 1000); // 1 минуту
        localStorage.setItem('hasTyped', expiryTime);
    }

    // Проверяем флаг и его срок действия
    var hasTyped = localStorage.getItem('hasTyped');
    var currentTime = new Date().getTime();

    if (!hasTyped || currentTime > hasTyped) {
        // Если флага нет или его срок действия истек, запускаем анимацию набора текста
        var typed = new Typed('#typing', {
            strings: ["Приветствуем вас", "Рады видеть вас"],
            typeSpeed: 50, // скорость печатания
            backSpeed: 50, // скорость стирания
            startDelay: 500, // задержка перед началом печатания
            loop: false, // отключаем повторение
            onComplete: function () {
                // Устанавливаем флаг в localStorage после завершения набора текста
                setTypedFlag();
            }
        });
    } else {
        // Если флаг установлен и его срок действия не истек, просто устанавливаем текст
        document.getElementById('typing').textContent = "Приветствуем вас";
    }
});
