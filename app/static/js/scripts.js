document.getElementById('registerForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: data.error,
                allowOutsideClick: false,
            });
        } else if (data.success) {
            Swal.fire({
                icon: 'success',
                title: '¡Registro Exitoso!',
                text: 'Los jugadores han sido registrados correctamente.',
                allowOutsideClick: false,
            }).then(() => {
                window.location.href = `/play?game_id=${data.game_id}`;
            });
        }
    })
    .catch(error => {
        Swal.fire({
            icon: 'error',
            title: 'Error inesperado',
            text: 'Ocurrió un error, intenta nuevamente.',
            allowOutsideClick: false,
        });
    });
});


const gameId = document.getElementById('moveForm').getAttribute('data-game-id');
document.getElementById('moveForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.error || 'Error inesperado');
            });
        }
        return response.json();
    })
    .then(data => {
        // Manejar la respuesta exitosa
        if (data.success) {
        } else if (data.game_over) {
            Swal.fire({
                title: '¡Juego Terminado!',
                text: 'Deseas repetir el juego o iniciar uno nuevo.',
                icon: 'question',
                showCancelButton: true,
                confirmButtonText: 'Repetir Juego',
                cancelButtonText: 'Iniciar Nuevo Juego',
            }).then((result) => {
                if (result.isConfirmed) {
                    $.post(`/reset/${data.game_id}`, function() {
                        window.location.href = `/play?game_id=${data.game_id}`;
                    });
                } else {
                    window.location.href = '/register';
                }
            });
        }
    })
    .catch(error => {
        Swal.fire({
            icon: 'error',
            title: 'Error inesperado',
            text: error.message || 'Ocurrió un error, intenta nuevamente.',
        });
    });
});



