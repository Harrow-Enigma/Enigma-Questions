<template>
  <main>
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item bg-dark">
        <h2 class="accordion-header" id="flush-headingOne">
          <button
            class="accordion-button collapsed bg-dark text-white"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#flush-collapseOne"
            aria-expanded="false"
            aria-controls="flush-collapseOne"
          >
            <h1>Question {{ $route.params.number }}</h1>
          </button>
        </h2>
        <div
          id="flush-collapseOne"
          class="accordion-collapse collapse show"
          aria-labelledby="flush-headingOne"
        >
          <div class="accordion-body">
            <nuxt-content :document="page" />
          </div>
        </div>
      </div>
      <div class="accordion-item bg-dark">
        <h2 class="accordion-header" id="flush-headingTwo">
          <button
            class="accordion-button collapsed bg-dark text-white"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#flush-collapseTwo"
            aria-expanded="false"
            aria-controls="flush-collapseTwo"
          >
            <h1>Submit Solution</h1>
          </button>
        </h2>
        <div
          id="flush-collapseTwo"
          class="accordion-collapse collapse"
          aria-labelledby="flush-headingTwo"
        >
          <div class="accordion-body">
            <div class="py-3">
              <h3>Python AutoSolution</h3>
              <AutoSolution :page="page" />
            </div>
            <div class="py-3">
              <h3>Alternative Solution Languages</h3>
              <p class="fs-5 col-md-8">
                Still Being Built, Meanwhile; Email us.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <hr class="my-5" />

    <div class="row g-5">
      <div class="col-md-6">
        <h2>Stuck?</h2>
        <p>
          {{ page.hint }}
        </p>
      </div>

      <div class="col-md-6">
        <h2>Details</h2>
        <p>Details regarding the question</p>
        <table class="table table-dark table-striped">
          <tbody>
            <tr>
              <td>Created</td>
              <td>{{ formatDate(page.createdAt) }}</td>
            </tr>
            <tr>
              <td>Updated</td>
              <td>{{ formatDate(page.updatedAt) }}</td>
            </tr>
            <tr>
              <td>Original Deadline</td>
              <td>{{ page.deadline }}</td>
            </tr>
            <tr>
              <td>Made by</td>
              <td>{{ page.creator }}</td>
            </tr>
            <tr v-if="!!page.functionname">
              <td>Function Name</td>
              <td>{{ page.functionname + "()" }}</td>
            </tr>
            <tr>
              <td>Path</td>
              <td>{{ page.path }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script>
import AutoSolution from "../../components/AutoSolution.vue";
export default {
  data() {
    return {
      loaded: false,
      tests: [],
    };
  },
  methods: {
    async getQuestion({ params }) {
      let res = await this.$store.dispatch("getQuestions");
      this.questions = res.data;
    },
  },
  /*
  async asyncData({ params, $content }) {
    const page = await $content("questions/" + params.number).fetch();
    return {
      page,
    };
  },
  methods: {
    formatDate(date) {
      const options = { year: "numeric", month: "long", day: "numeric" };
      return (
        new Date(date).toLocaleDateString("en-GB", options) +
        " " +
        new Date(date).toLocaleTimeString("en-GB")
      );
    },
  }, */
  components: { AutoSolution },
};
</script>

<style>
.accordion-body {
  background-color: #343a40;
}
</style>
