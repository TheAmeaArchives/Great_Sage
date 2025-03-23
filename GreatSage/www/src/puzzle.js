document.addEventListener("DOMContentLoaded", () => {
  const puzzleContainer = document.getElementById("puzzle");

  let pieces = Array.from({ length: 9 }, (_, i) => ({
    id: i,
    position: i,
    isCompleted: i === 0,
  }));

  function renderPuzzle() {
    puzzleContainer.innerHTML = "";
    pieces.forEach((piece) => {
      const div = document.createElement("div");
      div.className = `relative size-40 flex justify-center items-center text-lg font-bold
                transition-all duration-200 rounded-md
                ${
                  piece.isCompleted
                    ? "bg-red-500 text-white cursor-default"
                    : "bg-gray-300 hover:bg-gray-400 cursor-pointer"
                }`;

      div.textContent = piece.id;
      div.setAttribute("draggable", !piece.isCompleted);
      div.dataset.position = piece.position;

      div.addEventListener("click", () => completePiece(piece.id));
      div.addEventListener("dragstart", (e) => handleDragStart(e, piece.id));
      div.addEventListener("dragover", (e) => e.preventDefault());
      div.addEventListener("drop", (e) => handleDrop(e, piece.id));

      // Connectors for left, top, right, bottom
      const row = Math.floor(piece.position / 3);
      const col = piece.position % 3;

      // Create connector elements and set them as data attributes to reference later
      const connectors = {
        left: null,
        top: null,
        right: null,
        bottom: null,
      };

      // Left connector (not for leftmost pieces)
      if (col > 0) {
        const leftConnector = document.createElement("div");
        leftConnector.className =
          "absolute -left-2 top-1/2 w-4 h-6 rounded-full transform -translate-y-1/2";
        leftConnector.style.backgroundColor = piece.isCompleted
          ? "#ef4444"
          : "#d1d5db";
        div.appendChild(leftConnector);
        connectors.left = leftConnector;
      }

      // Top connector (not for top row)
      if (row > 0) {
        const topConnector = document.createElement("div");
        topConnector.className =
          "absolute top-0 left-1/2 h-4 w-6 rounded-full transform -translate-y-1/2 -translate-x-1/2";
        topConnector.style.backgroundColor = piece.isCompleted
          ? "#ef4444"
          : "#d1d5db";
        div.appendChild(topConnector);
        connectors.top = topConnector;
      }

      // Right connector (not for rightmost pieces)
      if (col < 2) {
        const rightConnector = document.createElement("div");
        rightConnector.className =
          "absolute -right-2 top-1/2 w-4 h-6 rounded-full transform -translate-y-1/2";
        rightConnector.style.backgroundColor = piece.isCompleted
          ? "#ef4444"
          : "#d1d5db";
        div.appendChild(rightConnector);
        connectors.right = rightConnector;
      }

      // Bottom connector (not for bottom row)
      if (row < 2) {
        const bottomConnector = document.createElement("div");
        bottomConnector.className =
          "absolute bottom-0 left-1/2 h-4 w-6 rounded-full transform translate-y-1/2 -translate-x-1/2";
        bottomConnector.style.backgroundColor = piece.isCompleted
          ? "#ef4444"
          : "#d1d5db";
        div.appendChild(bottomConnector);
        connectors.bottom = bottomConnector;
      }

      // Hover effects for connectors
      div.addEventListener("mouseenter", () => {
        if (connectors.left) connectors.left.style.backgroundColor = "#9ca3af";
        if (connectors.top) connectors.top.style.backgroundColor = "#9ca3af";
        if (connectors.right)
          connectors.right.style.backgroundColor = "#9ca3af";
        if (connectors.bottom)
          connectors.bottom.style.backgroundColor = "#9ca3af";
      });

      div.addEventListener("mouseleave", () => {
        if (connectors.left)
          connectors.left.style.backgroundColor = piece.isCompleted
            ? "#ef4444"
            : "#d1d5db";
        if (connectors.top)
          connectors.top.style.backgroundColor = piece.isCompleted
            ? "#ef4444"
            : "#d1d5db";
        if (connectors.right)
          connectors.right.style.backgroundColor = piece.isCompleted
            ? "#ef4444"
            : "#d1d5db";
        if (connectors.bottom)
          connectors.bottom.style.backgroundColor = piece.isCompleted
            ? "#ef4444"
            : "#d1d5db";
      });

      puzzleContainer.appendChild(div);
    });
  }

  function completePiece(id) {
    pieces = pieces.map((p) => (p.id === id ? { ...p, isCompleted: true } : p));
    renderPuzzle();
  }

  function handleDragStart(e, id) {
    e.dataTransfer.setData("text/plain", id);
  }

  function handleDrop(e, targetId) {
    const draggedId = parseInt(e.dataTransfer.getData("text/plain"));
    if (draggedId === targetId) return;

    const draggedPiece = pieces.find((p) => p.id === draggedId);
    const targetPiece = pieces.find((p) => p.id === targetId);

    // Swap positions
    [draggedPiece.position, targetPiece.position] = [
      targetPiece.position,
      draggedPiece.position,
    ];

    // Update UI
    pieces.sort((a, b) => a.position - b.position);
    renderPuzzle();
  }

  renderPuzzle();
});
