/*
 * Remove item from cart by setting qty value to 0 in update form and submitting it 
 * */ 

$('.remove-from-cart').click(function(e) {
        let articleId = $(this).attr('id');
        let size = $(this).data('size');
        let qty = 0;

        $(".update-form-field").attr('data-article_id', 'articleId')
            .attr('size', size)
            .attr('name', 'qty')
            .attr('value', qty)
            .appendTo('#update-form');
        $('#update-form').submit(); 
        Swal.fire({title: 'Removed !',
        showConfirmButton: false});    
});
