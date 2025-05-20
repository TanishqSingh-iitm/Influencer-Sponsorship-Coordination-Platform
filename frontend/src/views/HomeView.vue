<script setup>

</script>

<template>
 <nav class="navbar">
  <div class="container">
    <a href="https://flowbite.com/" class="brand">
      <img src="https://flowbite.com/docs/images/logo.svg" class="logo" alt="Flowbite Logo" />
      <span class="brand-name">Flowbite</span>
    </a>
    <div class="user-actions">
      <button type="button" class="user-menu-button" id="user-menu-button" aria-expanded="false">
        <span class="sr-only">Open user menu</span>
        
      </button>
      <div class="user-dropdown" id="user-dropdown">
        <div class="user-info">
          <span class="user-name">Bonnie Green</span>
          <span class="user-email">name@flowbite.com</span>
        </div>
        <ul class="user-menu" aria-labelledby="user-menu-button">
          <li><a href="#">Dashboard</a></li>
          <li><a href="#">Settings</a></li>
          <li><a href="#">Earnings</a></li>
          <li><a href="#">Sign out</a></li>
        </ul>
      </div>
      <button type="button" class="menu-toggle-button" aria-controls="navbar-menu" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="menu-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15" />
        </svg>
      </button>
    </div>
    <div class="navbar-menu" id="navbar-menu">
      <ul class="nav-links">
        <li><a href="#" class="active">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Pricing</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </div>
  </div>
</nav>

</template>
<style>

.container {
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.navbar {
  background-color: white;
  border-bottom: 1px solid #e2e8f0;
  padding: 1rem;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.brand {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo {
  height: 2rem;
  margin-right: 1rem;
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 600;
  color: black;
}

.user-actions {
  display: flex;
  align-items: center;
}

.user-menu-button {
  display: flex;
  align-items: center;
  background-color: #1f2937;
  border-radius: 50%;
  padding: 0.5rem;
  cursor: pointer;
  border: none;
}

.user-photo {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
}

.user-dropdown {
  display: none;
  position: absolute;
  right: 1rem;
  top: 3.5rem;
  background-color: white;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  z-index: 50;
}

.user-info {
  padding: 1rem;
}

.user-name {
  display: block;
  font-size: 1rem;
  color: black;
}

.user-email {
  display: block;
  font-size: 0.875rem;
  color: #6b7280;
}

.user-menu {
  list-style: none;
  margin: 0;
  padding: 0.5rem 0;
}

.user-menu li {
  padding: 0.5rem 1rem;
}

.user-menu li a {
  display: block;
  text-decoration: none;
  color: #374151;
  padding: 0.5rem 0;
}

.user-menu li a:hover {
  background-color: #f9fafb;
  color: #1f2937;
}

.menu-toggle-button {
  display: none;
  align-items: center;
  padding: 0.5rem;
  border: none;
  background: none;
  cursor: pointer;
}

.menu-icon {
  width: 1.25rem;
  height: 1.25rem;
}

.navbar-menu {
  display: flex;
  align-items: center;
}

.nav-links {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-links li {
  margin: 0 1rem;
}

.nav-links li a {
  text-decoration: none;
  color: black;
  padding: 0.5rem 1rem;
}

.nav-links li a:hover {
  background-color: #f0f4f8;
  border-radius: 0.25rem;
}

.nav-links li a.active {
  color: #1d4ed8;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .navbar-menu {
    display: none;
  }
  .menu-toggle-button {
    display: inline-flex;
  }
}

</style>