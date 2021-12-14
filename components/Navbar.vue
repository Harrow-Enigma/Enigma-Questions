<template>
  <div>
    <header class="align-items-center mb-3 border-bottom">
      <div class="row align-items-center pb-3">
        <div class="col-2">
          <img
            class="d-block mx-auto rounded"
            src="https://avatars.githubusercontent.com/u/72358647?s=400&amp;u=51ba6d2fd629ca470002c077d97f3d12499c1ed5&amp;v=4"
            alt=""
            width="100"
            height="auto"
          />
        </div>
        <div class="col-4">
          <h1 class="animate__animated animate__pulse">The Enigma Questions</h1>
        </div>
        <div class="col">
          <p
            class="fs-5 px-2 d-none d-sm-block animate__animated animate__pulse animate__delay-1s"
            style="margin-bottom: 0px"
          >
            A series of computational problems by Team Enigma.
          </p>
        </div>
      </div>
    </header>

    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item">
          <NuxtLink class="page-link" to="/"
            ><i class="material-icons" style="font-size: inherit">home</i>
          </NuxtLink>
        </li>
        <li class="page-item">
          <NuxtLink class="page-link" to="/problems/1">1</NuxtLink>
        </li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#">Next</a></li>
      </ul>
    </nav>
  </div>
</template>

<style scoped>
.pagination .page-link {
  background: #212529;
  color: white;
}

.pagination .nuxt-link-exact-active {
  color: black;
  background-color: #dee2e6 !important;
  border: solid 1px white !important;
}
</style>

<script></script>
