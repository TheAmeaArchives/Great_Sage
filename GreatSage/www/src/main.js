import "./style.css";

let game = (index) => `
<div class="flex gap-4 items-center">
<div
class="size-20 border rounded-xl bg-white border-gray-300"
></div>
<div
class="flex-1 p-2 px-4 border rounded-xl bg-white border-gray-300 flex gap-2"
>
<div>
   <h1 class="font-semibold text-lg">
       Nothing ${index}
   </h1>
   <p
       class="text-xs text-gray-500 line-clamp-2"
   >
       Lorem ipsum dolor sit amet,
       consectetur adipiscing elit.
   </p>
</div>
<div
   class="h-16 min-w-16 flex items-end justify-center gap-2"
>
   <img
       src="/heart.svg"
       alt="Heart Icon"
       class="size-3"
   />
   <img
       src="/share.svg"
       alt="Share Icon"
       class="size-3"
   />
   <img
       src="/bookmark.svg"
       alt="Bookmark Icon"
       class="size-3"
   />
</div>
</div>
</div>`;

document.addEventListener("DOMContentLoaded", () => {
  const indexScreen = document.getElementById("index-screen");
  const homeScreen = document.getElementById("home-screen");

  const menu = document.getElementById("menu");
  const games = document.getElementById("games");

  Array.from({ length: 3 }).map((_, index) => {
    const item = document.createElement("div");
    item.classList.add("menu-item");
    menu.appendChild(item);
    return item;
  });

  Array.from({ length: 10 }).forEach((_, index) => {
    games.innerHTML += game(index + 1);
  });

  homeScreen.classList.add("hidden");

  setTimeout(() => {
    indexScreen.classList.add("fade-out");

    indexScreen.addEventListener("animationend", () => {
      indexScreen.remove();

      homeScreen.classList.remove("hidden");
      homeScreen.classList.add("fade-in");
    });
  }, 2000);
});
