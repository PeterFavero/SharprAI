window.cameraId = "rusty-camera";
window.camera = document.getElementById(cameraId);
console.log("HELP ME 7");

// check if camera exists
if (window.camera) {
  console.log("camera found", camera);
  // make sure it is visible
  document.querySelector("#rusty-camera").style.display = "block";
} else {
  const camaeraElement = document.createElement("iframe");
  camaeraElement.id = cameraId;
  camaeraElement.setAttribute(
    "style",
    `
  all: initial;
  
  width:200px;
  height:200px;
  
  border-radius: 100px;
  
  z-index: 999999;
  border:none;
  `
  );

  // set permiissions on iframe - camera and microphone
  camaeraElement.setAttribute("allow", "camera");

  camaeraElement.src = chrome.runtime.getURL("camera.html");
  document.body.appendChild(camaeraElement);
  document.querySelector("#rusty-camera").style.display = "block";
}
