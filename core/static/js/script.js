document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modal-img");
    const modalTitle = document.getElementById("modal-title");
    const modalDescription = document.getElementById("modal-description");
    const closeBtn = document.querySelector(".close");

    // Data for events
    const events = [
        {
            img: "https://i.ibb.co/6cryq1nJ/book-fair.jpg",
            title: "Book Exchange Fair",
            description: "Join us at the Book Exchange Fair, where students can swap textbooks and novels in a vibrant and interactive environment. This event encourages students to declutter their shelves and discover new reads without spending a dime. Bring your pre-loved books and find new ones while connecting with fellow students. It’s a fantastic opportunity to save money and promote sustainability on campus. Don’t miss the chance to expand your library and engage in literary discussions with peers. Whether you’re looking for academic texts or leisure reads, this fair has something for everyone.",
        },
        {
            img: "https://i.ibb.co/84B29hd5/inter.jpg",
            title: "Interview Preparation Workshop",
            description: "Prepare for your future with our Interview Preparation Workshop designed specifically for Alliance University students. This engaging session covers essential tips and strategies to ace interviews in various fields. Our experienced facilitators will guide you through mock interviews, provide personalized feedback, and help you build confidence. You’ll learn how to articulate your strengths, tackle common interview questions, and present yourself professionally. This workshop offers a supportive environment where you can practice and refine your skills with peers. Equip yourself with the tools you need to impress potential employers and land your dream job.",
        },
        {
            img: "https://i.ibb.co/B5qKtRFJ/portal.jpg",
            title: "Student Portal Launch",
            description: "We are excited to announce the launch of the new Student Portal, a dynamic platform designed to enhance your campus experience. This portal will serve as a hub for discussions, event postings, and student engagement. You can easily connect with classmates, share ideas, and stay updated on campus happenings. The user-friendly interface makes navigation seamless, ensuring you find the information you need quickly. Get ready to participate in vibrant discussions and contribute to the university community. Your input and engagement are vital for creating a lively campus atmosphere, and this portal is your gateway to making it happen.",
        },
    ];

    // Function to open modal
    window.openModal = function (index) {
        modalImg.src = events[index].img;
        modalTitle.innerText = events[index].title;
        modalDescription.innerText = events[index].description;
        modal.style.display = "block";
    };

    // Function to close modal
    window.closeModal = function () {
        modal.style.display = "none";
    };

    // Close modal when clicking outside
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    // Close modal when clicking the close button
    closeBtn.addEventListener("click", closeModal);
});
