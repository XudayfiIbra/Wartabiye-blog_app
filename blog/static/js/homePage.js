document.addEventListener('DOMContentLoaded', () => {
    const searchItem = document.getElementById('search-item');
    const blogs = document.querySelectorAll('.blog');
    const home = document.getElementById('home')
    const tags = document.querySelectorAll('.tag')
    let hasVisible = false;

    const filterBlogs = () => {
        const searchedItem = searchItem.value.toLowerCase();

        blogs.forEach((blog) => {
            const blogTitle = blog.getAttribute('data-name').toLowerCase();
            const blogMatched = blogTitle.includes(searchedItem);
            

            if (blogMatched) {
                blog.style.display = "";
                
            } else {
                blog.style.display = "none";
                home.style.height = "100vh";
                console.log('is not matched');
            }
        });
    };

    tags.forEach((tag) => {
        tag.addEventListener('click', function() {
            const selectedTag = this.getAttribute('data-tag');

            blogs.forEach((blog) => {
                const BlogTag = blog.getAttribute('data-tags');

                if(BlogTag.includes(selectedTag)) {
                    blog.style.display = ''
                } else {
                    blog.style.display = "none"
                }
            })
        })
    })


    searchItem.addEventListener('keyup', filterBlogs);
});




// filter click
function handleClick(element) {
    document.querySelectorAll("li").forEach((li) => li.classList.remove("active"));
    element.classList.add("active");

    if (element.textContent.trim() === "All") {
        document.querySelectorAll(".blog").forEach((blog) => {
            blog.style.display = "";
        });
    }
}

// Mouse hover effect
if (typeof cursor === 'undefined') { // Ensure cursor is declared only once
    const cursor = new MouseFollower({
        container: document.body,
        speed: 0.3,
        innerClassName: "mf-cursor-inner",
    });
}


