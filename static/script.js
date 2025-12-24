document.addEventListener('DOMContentLoaded', () => {
    fetchQuote();
});

async function fetchQuote() {
    const quoteText = document.getElementById('quote-text');
    const authorText = document.getElementById('author-text');
    const body = document.body;
    const button = document.getElementById('new-quote-btn');

    // Butonu geçici olarak kilitle
    button.disabled = true;
    button.innerText = "Yükleniyor...";

    try {
        const response = await fetch('/api/quote');
        const data = await response.json();

        // Metinleri güncelle
        quoteText.innerText = `"${data.text}"`;
        authorText.innerText = `- ${data.author}`;
        
        // Arka plan rengini güncelle
        body.style.background = data.theme;

    } catch (error) {
        console.error('Hata:', error);
        quoteText.innerText = "Bir hata oluştu.";
        authorText.innerText = "";
    } finally {
        // Butonu tekrar aktif et
        button.disabled = false;
        button.innerText = "Yeni Söz Getir";
    }
}
