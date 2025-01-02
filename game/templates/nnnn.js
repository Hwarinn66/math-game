async function submitAnswer() {
    // Pastikan soal sudah di-load
    if (typeof num1 === 'undefined' || typeof num2 === 'undefined') {
        console.error('Question not loaded properly.');
        return;
    }

    const userAnswer = parseInt(answerInput.value, 10);
    totalAnswers += 1;

    // Periksa apakah input adalah angka dan bandingkan dengan jawaban benar
    if (!isNaN(userAnswer)) {
        if (userAnswer === num1 * num2) {
            correctAnswers += 1;
        }
    } else {
        console.error('Invalid input: Please enter a number.');
    }

    answerInput.value = ''; // Reset input
    await fetchQuestion();  // Load pertanyaan baru
}
