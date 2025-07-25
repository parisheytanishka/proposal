<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Heartfelt Proposal</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: #ffe6f0; /* Light pink background */
            /* Subtle repeating heart pattern */
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Cpath d='M50 85L45 80C20 60 0 45 0 25C0 10 10 0 25 0C35 0 40 5 50 15C60 5 65 0 75 0C90 0 100 10 100 25C100 45 80 60 55 80L50 85Z' fill='%23ffc0cb' opacity='0.1'/%3E%3C/svg%3E");
            background-size: 50px 50px; /* Adjust size for density of hearts */
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1rem; /* Responsive padding */
            overflow: hidden; /* Prevent scroll if content overflows slightly */
        }
        .screen-container {
            background-color: #ffffff;
            border-radius: 1.5rem; /* More rounded corners */
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04); /* Deeper shadow */
            padding: 2.5rem; /* Increased padding */
            max-width: 90%; /* Max width for responsiveness */
            width: 600px; /* Fixed width for larger screens */
            text-align: center;
            animation: fadeIn 1.5s ease-out; /* Fade-in animation */
            display: flex; /* Use flex for centering content within the card */
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 300px; /* Ensure a minimum height for all screens */
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .proposal-text {
            color: #333;
            line-height: 1.75; /* Improved readability */
        }
        .heart-icon {
            animation: pulse 1.5s infinite alternate; /* Pulsing heart animation */
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.1); }
        }
        .btn {
            transition: all 0.3s ease-in-out; /* Smooth transitions for buttons */
            position: relative; /* For sparkle effect */
            overflow: hidden;
        }
        .btn:hover {
            transform: translateY(-3px); /* Lift effect on hover */
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2); /* Deeper shadow on hover */
        }
        .btn:active {
            transform: translateY(0);
        }
        /* Sparkle effect on buttons */
        .btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: width 0.4s ease-out, height 0.4s ease-out, opacity 0.4s ease-out;
        }
        .btn:hover::before {
            width: 200%;
            height: 200%;
            opacity: 1;
        }

        /* Custom message box styles */
        .custom-message-box {
            background-color: #e6fffa; /* Light teal for success message */
            border-left: 5px solid #38b2ac; /* Teal border */
            color: #2c5282; /* Darker blue text */
            padding: 1rem;
            margin-top: 1.5rem;
            border-radius: 0.5rem;
            font-weight: 600;
            display: none; /* Hidden by default */
            animation: slideIn 0.5s ease-out;
            width: 100%; /* Full width within its container */
            position: fixed; /* Fixed position for pop-up */
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 100; /* On top of other content */
            max-width: 400px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            text-align: center;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translate(-50%, -60%); }
            to { opacity: 1; transform: translate(-50%, -50%); }
        }

        /* Hide all screens by default, JavaScript will show the initial one */
        .screen {
            display: none;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="screen-container" id="mainContainer">

        <!-- Initial Screen -->
        <div id="initialScreen" class="screen">
            <h1 class="text-4xl font-extrabold text-red-500 mb-6 flex items-center justify-center">
                <span class="heart-icon mr-3">💌</span> I want to express my feelings to you.
            </h1>
            <p class="proposal-text text-2xl mb-8 text-gray-700 font-semibold">
                Will you listen?
            </p>
            <div class="flex justify-center space-x-6">
                <button id="yesInitialBtn"
                        class="btn bg-gradient-to-r from-green-500 to-teal-600 text-white font-bold py-3 px-6 rounded-full text-xl shadow-lg hover:from-green-600 hover:to-teal-700 focus:outline-none focus:ring-4 focus:ring-green-300">
                    Yes
                </button>
                <button id="noInitialBtn"
                        class="btn bg-gradient-to-r from-gray-500 to-gray-600 text-white font-bold py-3 px-6 rounded-full text-xl shadow-lg hover:from-gray-600 hover:to-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-300">
                    No
                </button>
            </div>
        </div>

        <!-- Feelings Screen (shown if Yes is clicked on initial screen) -->
        <div id="feelingsScreen" class="screen">
            <h2 class="text-4xl font-extrabold text-pink-600 mb-6 flex items-center justify-center">
                <span class="heart-icon mr-3">💖</span> Being in love feels like magic.
            </h2>
            <p class="proposal-text text-xl mb-4 text-gray-700">
                It's butterflies in the stomach, a smile without reason, and warmth in the heart.
            </p>
            <p class="proposal-text text-xl mb-8 text-gray-700">
                It's the thought of someone special lighting up your day.
            </p>
            <button id="feelingsYesBtn"
                    class="btn bg-gradient-to-r from-purple-500 to-indigo-600 text-white font-bold py-3 px-6 rounded-full text-xl shadow-lg hover:from-purple-600 hover:to-indigo-700 focus:outline-none focus:ring-4 focus:ring-purple-300">
                Yes
            </button>
        </div>

        <!-- Rejection Screen (shown if No is clicked on initial screen) -->
        <div id="rejectionScreen" class="screen">
            <h2 class="text-4xl font-extrabold text-gray-700 mb-6 flex items-center justify-center">
                <span class="mr-3">😢</span> Oh no!
            </h2>
            <p class="proposal-text text-xl mb-8 text-gray-700">
                Can you tell me why?
            </p>
            <input type="text" id="reasonInput" placeholder="Enter your reason here..."
                   class="w-full p-3 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400">
            <button id="submitReasonBtn"
                    class="btn bg-gradient-to-r from-blue-500 to-blue-600 text-white font-bold py-3 px-6 rounded-full text-xl shadow-lg hover:from-blue-600 hover:to-blue-700 focus:outline-none focus:ring-4 focus:ring-blue-300">
                Submit
            </button>
        </div>

    </div>

    <!-- Custom Message Boxes (replacing messagebox.showinfo) -->
    <div id="loveMessageBox" class="custom-message-box">
        <h3 class="text-3xl font-bold mb-2">Confession</h3>
        <p class="text-lg">I love you ❤️</p>
        <button onclick="this.parentNode.style.display='none'" class="mt-4 bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600">Close</button>
    </div>

    <div id="thanksMessageBox" class="custom-message-box">
        <h3 class="text-3xl font-bold mb-2">Thanks</h3>
        <p class="text-lg">Thanks for being honest 💔</p>
        <button onclick="this.parentNode.style.display='none'" class="mt-4 bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600">Close</button>
    </div>

    <script>
        // Get references to all screen elements and buttons
        const initialScreen = document.getElementById('initialScreen');
        const feelingsScreen = document.getElementById('feelingsScreen');
        const rejectionScreen = document.getElementById('rejectionScreen');

        const yesInitialBtn = document.getElementById('yesInitialBtn');
        const noInitialBtn = document.getElementById('noInitialBtn');
        const feelingsYesBtn = document.getElementById('feelingsYesBtn');
        const submitReasonBtn = document.getElementById('submitReasonBtn');
        const reasonInput = document.getElementById('reasonInput');

        const loveMessageBox = document.getElementById('loveMessageBox');
        const thanksMessageBox = document.getElementById('thanksMessageBox');

        // Function to show a specific screen and hide others
        function showScreen(screenToShow) {
            initialScreen.style.display = 'none';
            feelingsScreen.style.display = 'none';
            rejectionScreen.style.display = 'none';
            loveMessageBox.style.display = 'none'; // Ensure message boxes are hidden
            thanksMessageBox.style.display = 'none';

            screenToShow.style.display = 'flex'; // Use flex to center content within the screen
        }

        // --- Event Listeners ---

        // Initial Screen: Yes button click
        yesInitialBtn.addEventListener('click', () => {
            showScreen(feelingsScreen);
        });

        // Initial Screen: No button click
        noInitialBtn.addEventListener('click', () => {
            showScreen(rejectionScreen);
        });

        // Feelings Screen: Yes button click
        feelingsYesBtn.addEventListener('click', () => {
            loveMessageBox.style.display = 'block'; // Show the "I Love You" message box
            // No need to disable button or change text here, as it's a final message.
        });

        // Rejection Screen: Submit button click
        submitReasonBtn.addEventListener('click', () => {
            const reason = reasonInput.value.trim();
            // In a real app, you might send this reason to a server.
            // For this demo, we just show the thanks message.
            thanksMessageBox.style.display = 'block';
            // No need to disable button or change text here, as it's a final message.
        });

        // --- Initial setup ---
        // Show the initial screen when the page loads
        document.addEventListener('DOMContentLoaded', () => {
            showScreen(initialScreen);
        });
    </script>
</body>
</html>
