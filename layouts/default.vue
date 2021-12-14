<template>
  <div style="font-family: 'Readex Pro', sans-serif">
    <div class="col-lg-8 mx-auto p-3 py-md-5">
      <Navbar />
      <Nuxt />
      <Footer />
    </div>
  </div>
</template>

<style lang="css">
body {
  background-color: black;
  color: white;
}
h1 {
  font-weight: 600;
}
p {
  font-weight: 300;
}
h2 {
  font-weight: 500;
}
html {
  scroll-behavior: smooth;
}

::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: #000000;
}

::-webkit-scrollbar {
  width: 12px;
  background-color: #000000;
}

::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #212529;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
