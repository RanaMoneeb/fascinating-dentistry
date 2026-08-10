/**
 * Infinite scroll for blog listing pages.
 * Works with the Django Paginator ?page=N query parameter.
 * Appends new post cards to #post-grid and removes the load-more button
 * when no more pages remain.
 */
(function () {
    "use strict";

    var grid = document.getElementById("post-grid");
    if (!grid) return;

    var loadBtn = document.getElementById("load-more-btn") ||
        document.querySelector('a[href^="?page="]');

    if (!loadBtn) return;

    var nextUrl = loadBtn.getAttribute("href");
    var loading = false;

    function extractCards(html) {
        var tmp = document.createElement("div");
        tmp.innerHTML = html;
        var newGrid = tmp.querySelector("#post-grid");
        return newGrid ? newGrid.innerHTML : "";
    }

    function extractNextButton(html) {
        var tmp = document.createElement("div");
        tmp.innerHTML = html;
        var btn = tmp.querySelector('a[href^="?page="]');
        return btn ? btn : null;
    }

    function loadMore() {
        if (loading || !nextUrl) return;
        loading = true;

        // Visual feedback
        if (loadBtn) {
            loadBtn.textContent = "Loading...";
            loadBtn.style.opacity = "0.6";
        }

        fetch(nextUrl, {
            headers: { "X-Requested-With": "XMLHttpRequest" },
        })
            .then(function (resp) {
                if (!resp.ok) throw new Error("HTTP " + resp.status);
                return resp.text();
            })
            .then(function (html) {
                var cards = extractCards(html);
                if (cards) {
                    grid.insertAdjacentHTML("beforeend", cards);
                }

                // Check if there's another page after this one
                var newBtn = extractNextButton(html);
                if (newBtn && loadBtn) {
                    nextUrl = newBtn.getAttribute("href");
                    loadBtn.setAttribute("href", nextUrl);
                    loadBtn.textContent = "Load more articles";
                    loadBtn.style.opacity = "1";
                } else {
                    // No more pages -- remove the button
                    if (loadBtn && loadBtn.parentElement) {
                        loadBtn.parentElement.remove();
                    }
                    nextUrl = null;
                }

                loading = false;
            })
            .catch(function () {
                loading = false;
                if (loadBtn) {
                    loadBtn.textContent = "Load more articles";
                    loadBtn.style.opacity = "1";
                }
            });
    }

    // Click to load (always available)
    if (loadBtn) {
        loadBtn.addEventListener("click", function (e) {
            e.preventDefault();
            loadMore();
        });
    }

    // Auto-load on scroll (IntersectionObserver on the button)
    if ("IntersectionObserver" in window && loadBtn) {
        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting && !loading) {
                        loadMore();
                    }
                });
            },
            { rootMargin: "300px" }
        );
        observer.observe(loadBtn);
    }
})();
