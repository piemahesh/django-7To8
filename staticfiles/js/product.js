let deletedId = null;
const deleteModal = document.getElementById("deleteModal");

const yesBtn = document.querySelector(".yes");
const noBtn = document.querySelector(".no");

function onDelete(productId) {
  deleteModal.classList.add("open");
  deletedId = productId;
  console.log(deletedId);
  console.log("btn clicked");
}

function onClose() {
  deleteModal.classList.remove("open");
  deleteModal.classList.add("closed");
}

function onDeleteConfirm() {
  if (deletedId) {
    let link = document.createElement("a");
    link.href = `/product/delete/${deletedId}`;
    document.body.appendChild(link);
    link.click();
    link.remove();
  }
}

function onEdit(productId) {
  let link = document.createElement("a");
  link.href = `/product/edit/${productId}`;
  document.body.appendChild(link);
  link.click();
  link.remove();
}

noBtn.addEventListener("click", onClose);
yesBtn.addEventListener("click", onDeleteConfirm);
