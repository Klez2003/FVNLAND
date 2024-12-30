// Function to randomly select an image for meta tags (Open Graph & Twitter)
function getRandomImage() {
  const images = [
    'https://sadist.life/purple-juicewrld-2.jpg',
    'https://sadist.life/purple-juicewrld-3.jpg',
    'https://sadist.life/purple-juicewrld-4.jpg',
    'https://sadist.life/purple-juicewrld-5.jpg'
  ];
  const randomImage = images[Math.floor(Math.random() * images.length)];
  return randomImage;
}

// Update Open Graph meta tag for the image
function updateMetaTags() {
  const randomImage = getRandomImage();
  
  // Update the og:image meta tag dynamically
  const ogImageTag = document.getElementById('og-image');
  ogImageTag.setAttribute('content', randomImage);

  // Update the twitter:image meta tag dynamically
  const twitterImageTag = document.querySelector('meta[name="twitter:image"]');
  twitterImageTag.setAttribute('content', randomImage);
}

// Initialize the page with random image meta tags
window.onload = function () {
  updateMetaTags(); // Run the function when the page loads
};