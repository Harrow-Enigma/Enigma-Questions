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
        <div class="col d-none d-sm-block">
          <p
            class="fs-5 px-2 animate__animated animate__pulse animate__delay-1s"
            style="margin-bottom: 0px"
          >
            A series of computational problems by Team Enigma.
          </p>
        </div>
      </div>
    </header>

    <nav class="navbar mb-3 border-bottom">
      <div class="container-fluid">
        <ul class="pagination">
          <li class="page-item">
            <NuxtLink class="page-link" to="/"
              ><i class="material-icons" style="font-size: inherit">home</i>
            </NuxtLink>
          </li>
          <li
            class="page-item"
            v-for="question in questions"
            :key="question.slug"
          >
            <NuxtLink class="page-link" :to="'/problems/' + question.slug">
              {{ question.slug }}</NuxtLink
            >
          </li>
        </ul>

        <div class="text-end d-flex">
          <template v-if="!isAuthenticated">
            <nuxt-link
              type="button"
              class="btn btn-outline-light me-2"
              aria-current="page"
              to="/auth/login"
            >
              Login
            </nuxt-link>

            <nuxt-link
              type="button"
              class="btn btn-primary"
              aria-current="page"
              to="/auth/register"
            >
              Register
            </nuxt-link>
          </template>

          <template v-else>
            <a
              type="button"
              class="btn btn-outline-light me-2"
              aria-current="page"
              to="#"
              @click="logout"
            >
              Logout
            </a>

            <nuxt-link
              type="button"
              class="btn btn-warning me-2"
              aria-current="page"
              to="/profile"
            >
              Profile
            </nuxt-link>

            <nuxt-link
              v-if="isAuthenticatedAdmin"
              type="button"
              class="btn btn-danger me-2"
              aria-current="page"
              to="/admin"
            >
              Admin Console
            </nuxt-link>
          </template>
        </div>
      </div>
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

<script>
export default {
  methods: {
    async logout() {
      await this.$auth.logout();
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    isAuthenticatedAdmin() {
      return this.$store.getters.isAuthenticatedAdmin;
    }
  },
  /*
  async fetch() {
    this.questions = await this.$content("questions")
      .only(["slug"])
      .sortBy("createdAt", "asc")
      .fetch();
  },*/
  data() {
    return { questions: null };
  }
};
</script>
