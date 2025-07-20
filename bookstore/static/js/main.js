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
                    // Updates quantity text
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

    document.querySelectorAll(".edit-btn").forEach((button) => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            const commentId = button.getAttribute("data-id");
            const commentTextP = document.querySelector(`#comment-text-${commentId}`);
            const oldText = commentTextP.textContent;
            const deleteBtn = this.parentElement.querySelector(".delete-button");

            // Replaces <p> tag with <textarea> tag
            const textarea = document.createElement("textarea");
            textarea.rows = "5";
            textarea.cols = "50";
            textarea.value = oldText;
            commentTextP.replaceWith(textarea);

            // Replaces "Edit" button with "Save" button
            const saveBtn = document.createElement("a");
            saveBtn.classList.add("ms-4");
            saveBtn.style = "cursor: pointer";
            saveBtn.innerHTML =
                '<img class="comment-button" src="/static/icons/diskette.png" alt="save button">';
            this.replaceWith(saveBtn);

            saveBtn.addEventListener("click", function () {
                const newText = textarea.value;

                fetch("/comments/update/", {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                    body: `comment_id=${commentId}&text=${encodeURIComponent(newText)}`,
                })
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.success) {
                            const newP = document.createElement("p");
                            newP.id = `comment-text-${commentId}`;
                            newP.textContent = data.updated_text;
                            textarea.replaceWith(newP);
                            saveBtn.replaceWith(button); // reuse original edit button
                            cancelBnt.replaceWith(deleteBtn);
                        } else {
                            alert("Error: " + data.error);
                        }
                    });
            });

            // Replaces "Delete" button with "Cancel" button
            const cancelBnt = document.createElement("a");
            cancelBnt.style = "cursor: pointer";
            cancelBnt.innerHTML =
                '<img class="comment-button" src="/static/icons/cancel.png" alt="cancel button">';
            deleteBtn.replaceWith(cancelBnt);

            cancelBnt.addEventListener("click", function () {
                textarea.replaceWith(commentTextP);
                saveBtn.replaceWith(button);
                cancelBnt.replaceWith(deleteBtn);
            });
        });
    });

    document.querySelectorAll(".delete-button").forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();

            const comment_id = button.getAttribute("data-id");

            fetch("/comments/delete/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: `comment_id=${comment_id}`,
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        const commentToDelete = button.closest(".comment-body");
                        if (commentToDelete) {
                            commentToDelete.remove();
                        }
                    } else {
                        alert("Error: " + data.error);
                    }
                });
        });
    });

    // Helper to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
