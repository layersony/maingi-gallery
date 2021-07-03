document.addEventListener('DOMContentLoaded', function () {
  const btns = document.querySelectorAll("[data-target]");
  const close_modals = document.querySelectorAll(".close-modal");
  const overlay = document.getElementById("overlay");
  const textcopy = document.querySelectorAll('.copylink')
  const btncopy = document.querySelectorAll('.btncopy')

  btns.forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelector(btn.dataset.target).classList.add("active");
      overlay.classList.add("active");
    });
  });

  close_modals.forEach((btn) => {
    btn.addEventListener("click", () => {
      const modal = btn.closest(".modal");
      modal.classList.remove("active");
      overlay.classList.remove("active");
    });
  });

  window.onclick = (event) => {
    if (event.target == overlay) {
      const modals = document.querySelectorAll(".modal");
      modals.forEach((modal) => modal.classList.remove("active"));
      overlay.classList.remove("active");
    }
  };

  textcopy.forEach((btn, i) => {
    btncopy[i].addEventListener("click", ()=>{
      p = btn.id.split("trial");
      var cptext = document.getElementById('trial'+p[1])
      cptext.select()      
      cptext.setSelectionRange(0, 99999)
      document.execCommand('copy')
      alert("Copied link: " + cptext.value);
    })
  });
})