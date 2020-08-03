/*
 * Remove item from cart by setting qty value to 0 in update form and submitting it 
 * */ 

$('.remove-from-cart').click(function(e) {
        let articleId = $(this).attr('id');
        let size = $(this).data('size');
        let qty = 0;

        $(".update-form-field").attr('data-article_is', 'articleId')
            .attr('size', size)
            .attr('name', 'qty')
            .attr('value', qty)
            .appendTo('#my-form');
        $('#update-form').submit();

    
})

/*
 * Increasing qty of an item added to the cart
 * */ 

$('.increase-qty').click(function(e) {
    e.preventDefault();
    var qtyField = $(this).closest('#qty-group').find('.update-form-field')[0];
    var currentQty = parseInt($(qtyField).val());
    
    if (currentQty < 10){
        currentQty ++;
    } else if ( currentQty = 10 ){
        currentQty = 1;
    }
    $(qtyField).val(currentQty);
        
 });