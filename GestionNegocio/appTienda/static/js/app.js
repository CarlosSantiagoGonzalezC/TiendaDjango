function modalEliminar(idProducto){
    Swal.fire({
        title: '¿Está seguro de eliminar?',
        text: "Usted está a punto de eliminar este producto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si',
        cancelButtonText: 'No'
    }).then((result) => {
        if (result.isConfirmed) {
            location.href = "/eliminarProducto/" + idProducto + "/"
        }
    })
}