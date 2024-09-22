function showEndGameAlert() {
    Swal.fire({
        title: '¡Juego Terminado!',
        text: '¿Deseas repetir el juego o iniciar uno nuevo?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Repetir Juego',
        cancelButtonText: 'Iniciar Nuevo Juego'
    }).then((result) => {
        if (result.isConfirmed) {
            location.reload();
        } else {
            window.location.href = '/register';
        }
    });
}

showEndGameAlert()