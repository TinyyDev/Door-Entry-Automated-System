// static/script.js

document.addEventListener("DOMContentLoaded", function() {
    const motionStatusElement = document.getElementById("motion-status");

    // Function to update motion status
    function updateMotionStatus() {
        // Replace this with your code to fetch motion sensor status
        // You might use AJAX or other methods here
        const motionStatus = "Motion Detected";  // Sample status, replace with actual data
        motionStatusElement.innerText = motionStatus;
    }

    // Initial status update
    updateMotionStatus();

    // Function to refresh the status at regular intervals (e.g., every 5 seconds)
    setInterval(function() {
        updateMotionStatus();
    }, 5000); // 5000 milliseconds = 5 seconds
});
