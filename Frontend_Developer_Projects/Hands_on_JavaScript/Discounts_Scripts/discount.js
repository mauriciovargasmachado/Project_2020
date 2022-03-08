
function final_price(price, discount){

    const discount_percentage = (price*discount)/100;
    
    const discount_price = price - discount_percentage;

    return discount_price;
    
}

function on_click_show_final_price(){

    const input_price = document.getElementById(input_price);
    const price_value = input_price.value;

    const input_discount= document.getElementById(input_discount);
    const discount_value = input_discount.value;

    const discount_price = final_price(price_value,discount_value);
}

const result = document.getElementById("resultP");
result.innerText = "The final price is: " + discount_price();

