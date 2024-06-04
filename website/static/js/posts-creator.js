let sectionCounter = 0;

function addSection(type) {
  const container = document.getElementById("sections");
  const section = document.createElement("div");
  section.classList.add("section");

  const label = document.createElement("label");
  const textarea = document.createElement("textarea");
  const input = document.createElement("input");

  if (type === "heading" || type === "text") {
    label.textContent = type === "heading" ? "Heading" : "Text";
    textarea.name = `${type}_content_${sectionCounter}`;
    textarea.required = true;
    section.appendChild(label);
    section.appendChild(textarea);
  } else if (type === "image") {
    label.textContent = "Image URL";
    input.type = "text";
    input.name = `image_content_${sectionCounter}`;
    input.required = true;
    section.appendChild(label);
    section.appendChild(input);
  } else if (type === "code") {
    label.textContent = "Code";
    textarea.name = `code_content_${sectionCounter}`;
    textarea.required = true;
    textarea.style.fontFamily = "monospace";
    section.appendChild(label);
    section.appendChild(textarea);
  }

  container.appendChild(section);
  sectionCounter++;
}
