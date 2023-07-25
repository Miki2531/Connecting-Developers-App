let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      // Get The Data attribute
      let page = this.dataset.page;

      // ADD HIDDEN SEARCH INPUT TO FROM
      searchForm.innerHTML += `<input value=${{
        page,
      }} name="page" hidden/>`;

      //SUBMIT FORM
      searchForm.submit();
    });
  }
}
