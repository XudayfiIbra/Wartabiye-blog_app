// active tag
function handleClick(element) {
    document.querySelectorAll("li").forEach((li) => li.classList.remove("active"));
    element.classList.add("active");

    if (element.textContent.trim() === "All") {
        document.querySelectorAll(".blog").forEach((blog) => {
            blog.style.display = "";
        });
    }
}


document.addEventListener('DOMContentLoaded', () => {
    const searchItem = document.getElementById('search-item');
    const blogs = document.querySelectorAll('.blog');
    const tags = document.querySelectorAll('.tag');

    const filterBlogs = () => {
        const searchedItem = searchItem.value.toLowerCase();

        blogs.forEach((blog) => {
            const blogTitle = blog.getAttribute('data-name').toLowerCase();
            const blogMatched = blogTitle.includes(searchedItem);

            if (blogMatched) {
                blog.style.display = "";
            } else {
                blog.style.display = "none";
            }
        });
    };

    const filterByTag = (selectedTag) => {
        blogs.forEach((blog) => {
            const blogTags = blog.getAttribute('data-tags').split(',').map(tag => tag.trim().toLowerCase());

            if (blogTags.includes(selectedTag)) {
                blog.style.display = '';
            } else {
                blog.style.display = 'none';
            }
        });
    };

    tags.forEach((tag) => {
        tag.addEventListener('click', function() {
            const selectedTag = this.getAttribute('data-tag');
            filterByTag(selectedTag);
        });
    });

    searchItem.addEventListener('keyup', filterBlogs);
});
