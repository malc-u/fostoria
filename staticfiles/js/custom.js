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
        Swal.fire({title: 'Removed !',
        showConfirmButton: false});    
})

/*
* Increasing qty of an item added to the cart. 
* Qty never goes above max set for the field as setting qty 
* to mX 10 and clicking increase again returns qty to 1 thus 
* allowing it only to go through 1-10 then returning to 1 and so on.
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

 /*
 * Decreasing qty of an item added to the cart.
 * Qty never goes to negative as setting qty to min 1  and clicking
 * decrease again returns qty to 10 thus allowing it only to go through 
 * 10-1 then returning to 10 and so on.
 * */ 

$('.decrease-qty').click(function(e) {
    e.preventDefault();
    var qtyField = $(this).closest('#qty-group').find('.update-form-field')[0];
    var currentQty = parseInt($(qtyField).val());
    
    if (currentQty > 1){
        currentQty --;
    } else if ( currentQty = 1 ){
        currentQty = 10;
    }
    $(qtyField).val(currentQty);
        
 });