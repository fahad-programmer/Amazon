const script = document.createElement("script");
script.type = "text/javascript";
script.src =
  "https://cdn.tiny.cloud/1/za0l7f6nq6sibw4odkhy9p4wjt1vi2zw9qfmby767kedbc25/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

script.onload = () => {
  tinymce.init({
    selector: "#id_description, #id_main_description, #id_warrenty_support",
    plugins: [
      "advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker",
      "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
      "table emoticons template paste help",
    ],
    toolbar:
      "undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | " +
      "bullist numlist outdent indent | link image | print preview media fullpage | " +
      "forecolor backcolor emoticons | help",
    menu: {
      favs: {
        title: "My Favorites",
        items: "code visualaid | searchreplace | spellchecker | emoticons",
      },
    },
    menubar: "favs file edit view insert format tools table help",
    content_css: "css/content.css",
  });
};
