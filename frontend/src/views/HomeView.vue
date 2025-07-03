<template>
  <div class="home-container">
    <div class="hero">
      <h1>Welcome to Quotely</h1>
      <p class="tagline">Discover, save, and share inspiring quotes from all around the world.</p>

      <div class="auth-buttons">
        <router-link to="/login" class="btn login-btn">Login</router-link>
        <router-link to="/register" class="btn register-btn">Register</router-link>
      </div>
    </div>

    <div class="info-section">
      <h2>Why Quotely?</h2>
      <ul>
        <li>🌟 Explore quotes by famous authors, topics, and moods.</li>
        <li>📝 Save your favorite quotes and revisit them anytime.</li>
        <li>💬 Share quotes with friends and inspire others.</li>
      </ul>

      <p class="note">You need to <strong>log in or create an account</strong> to access the full features of Quotely.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
.home-container {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.hero {
  background-color: #f0f8ff;
  padding: 2rem;
  border-radius: 10px;
}

.tagline {
  font-size: 1.2rem;
  margin-top: 1rem;
  color: #555;
}

.auth-buttons {
  margin-top: 2rem;
}

.btn {
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  margin: 0 1rem;
  border-radius: 5px;
  font-weight: bold;
  transition: background 0.3s;
}

.login-btn {
  background-color: #4CAF50;
  color: white;
}

.login-btn:hover {
  background-color: #45a049;
}

.register-btn {
  background-color: #008CBA;
  color: white;
}

.register-btn:hover {
  background-color: #007bb5;
}

.info-section {
  margin-top: 3rem;
  text-align: left;
}

.info-section h2 {
  margin-bottom: 1rem;
}

.info-section ul {
  list-style: none;
  padding-left: 0;
}

.info-section li {
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.note {
  margin-top: 1.5rem;
  font-style: italic;
  color: #888;
}
</style>
