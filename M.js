function loadPage(page) {
  const title = document.getElementById('page-title');
  const content = document.getElementById('page-content');

  if (page === 'home') {
    title.textContent = 'Beranda';
    content.innerHTML = '<p>Ini adalah halaman beranda.</p>';
  } else if (page === 'profile') {
    title.textContent = 'Profil';
    content.innerHTML = '<p>Ini adalah halaman profil pengguna.</p>';
  } else if (page === 'settings') {
    title.textContent = 'Pengaturan';
    content.innerHTML = '<p>Ini adalah halaman pengaturan.</p>';
  }
}