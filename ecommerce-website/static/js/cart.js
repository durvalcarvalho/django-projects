var updateBtns = document.getElementsByClassName('update-cart');


for(let btn of updateBtns) {
    btn.addEventListener('click', function() {
        const productId = btn.dataset.product_id;
        const product_qty_element = document.getElementById(`product_quantity_${productId}`);

        const product_row_element = document.getElementById(`product_row_${productId}`);
        const product_total_element = document.getElementById(`product_total_${productId}`);


        const action = btn.dataset.action;
        const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        addCookieItem(productId, action);

        if(user === 'AnonymousUser') {
            console.log("User is Anonymous");
            // alert("You must be logged in to update your cart");
            return;
        }

        const url = `/add-remove-one-to-cart/${productId}/${action}/`;

        $.ajax({
            url: url,
            headers: {'X-CSRFToken': csrf},
            type: 'POST',
            success: function(response) {
                let pathname = window.location.pathname;

                if(pathname === '/cart/') {
                    product_qty_element.innerHTML = response.quantity;
                    product_total_element.innerHTML = response.total;

                    if(response.quantity == 0) {
                        product_row_element.remove();
                    }
                }


            },
            error: function(response) {
                console.log("Error", response);
            }
        });
    });
}