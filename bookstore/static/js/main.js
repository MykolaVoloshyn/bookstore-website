document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".change-quantity").forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();

            const itemId = button.getAttribute("data-id");
            const isIncrease = button.classList.contains("increase");
            const url = isIncrease
                ? `/cart/increase_quantity/${itemId}/`
                : `/cart/decrease_quantity/${itemId}/`;

            fetch(url)
                .then((response) => response.json())
                .then((data) => {
                    // update quantity text
                    const totalBooksNumEl = document.getElementById("total-books-num");
                    const totalPriceEl = document.getElementById("total-price");
                    const quantityEl = document.getElementById(`quantity-${itemId}`);
                    const priceEl = document.getElementById(`price-${itemId}`);
                    if (totalBooksNumEl) {
                        totalBooksNumEl.textContent = data.total_books_num;
                    }
                    if (totalPriceEl) {
                        totalPriceEl.textContent = new Intl.NumberFormat("en-US", {
                            style: "currency",
                            currency: "USD",
                        }).format(data.total_price);
                    }
                    if (quantityEl) {
                        quantityEl.textContent = data.quantity;
                    }
                    if (priceEl) {
                        priceEl.textContent = new Intl.NumberFormat("en-US", {
                            style: "currency",
                            currency: "USD",
                        }).format(data.price);
                    }
                });
        });
    });
});
